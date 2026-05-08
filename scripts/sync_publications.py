"""
Sync publications from Google Scholar (via SerpAPI) to data/publications.yaml.

Uses the google_scholar_author endpoint with Ying Bi's author ID to fetch
the complete publication list from her verified Google Scholar profile.
Optionally uses DeepSeek API to infer paper categories.

Requirements:
    pip install requests pyyaml

Environment variables:
    SERPAPI_API_KEY     - SerpAPI key for Google Scholar (required)
    DEEPSEEK_API_KEY    - DeepSeek API key for category inference (optional)

Usage:
    SERPAPI_API_KEY=xxx python scripts/sync_publications.py
"""

import json
import os
import sys
import difflib
from pathlib import Path

import requests
import yaml


def _load_env_file():
    """Load .env file from project root if it exists (no third-party dependency)."""
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if not env_file.exists():
        return
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


_load_env_file()

SERPAPI_API_KEY = os.environ.get("SERPAPI_API_KEY")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
DEEPSEEK_MODEL = "deepseek-v4-flash"
AUTHOR_ID = "WI2ykPAAAAAJ"
PUBLICATIONS_FILE = Path("data/publications.yaml")
NUM_PER_PAGE = 100

CATEGORY_OPTIONS = ["专著/书籍", "综述论文", "期刊论文", "会议论文"]

CATEGORY_PROMPT = """Classify each paper below into exactly one category. Reply with a JSON array of strings, one per paper, in the same order.

Categories:
- "期刊论文": journal article (IEEE Trans, Elsevier, Springer journal, etc.)
- "会议论文": conference paper (CEC, GECCO, IVCNZ, SSCI, proceedings, etc.)
- "综述论文": survey / review paper (title or abstract mentions "survey", "review", "综述")
- "专著/书籍": book or monograph (publisher is Springer, MDPI, etc. AND it's a complete book, not a journal article)

Papers to classify:"""


def fetch_all_articles():
    """Fetch all articles from SerpAPI google_scholar_author with pagination."""
    articles = []
    start = 0
    page = 1

    while True:
        params = {
            "engine": "google_scholar_author",
            "author_id": AUTHOR_ID,
            "hl": "en",
            "api_key": SERPAPI_API_KEY,
            "num": NUM_PER_PAGE,
            "start": start,
            "sort": "pubdate",
        }
        resp = requests.get("https://serpapi.com/search.json", params=params)
        resp.raise_for_status()
        data = resp.json()

        batch = data.get("articles", [])
        articles.extend(batch)
        print(f"  Page {page}: {len(batch)} articles (start={start}), total: {len(articles)}")

        if len(batch) == 0:
            break

        pagination = data.get("serpapi_pagination") or data.get("pagination") or {}
        if not pagination.get("next"):
            break

        start += NUM_PER_PAGE
        page += 1

    return articles


def load_existing_pubs():
    """Load existing publications from YAML file."""
    if not PUBLICATIONS_FILE.exists():
        return []
    with open(PUBLICATIONS_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data if data else []


def title_similarity(t1, t2):
    """Calculate similarity ratio between two cleaned titles."""
    t1_clean = t1.lower().strip().rstrip(".")
    t2_clean = t2.lower().strip().rstrip(".")
    return difflib.SequenceMatcher(None, t1_clean, t2_clean).ratio()


def is_duplicate(article, existing_pubs):
    """Check if article already exists by title similarity."""
    new_title = article.get("title", "")
    if not new_title:
        return True
    for pub in existing_pubs:
        existing_title = pub.get("title", "")
        if not existing_title:
            continue
        if title_similarity(new_title, existing_title) > 0.85:
            return True
    return False


def map_article_to_pub(article):
    """Map a SerpAPI author article to the YAML publication format."""
    title = article.get("title", "")

    authors_raw = article.get("authors", "")
    if isinstance(authors_raw, str):
        authors = [a.strip() for a in authors_raw.split(",") if a.strip()]
    elif isinstance(authors_raw, list):
        authors = authors_raw
    else:
        authors = []

    year_str = article.get("year", "")
    try:
        year = int(str(year_str))
    except (ValueError, TypeError):
        year = 0

    return {
        "authors": authors,
        "title": title,
        "year": year,
        "publication": article.get("publication", ""),
        "url_custom": article.get("link", ""),
        "category": "期刊论文",  # fallback, will be overwritten by LLM inference
        "tags": [],
    }


def _call_deepseek(prompt):
    """Single DeepSeek API call. Returns response content string."""
    resp = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": DEEPSEEK_MODEL,
            "messages": [
                {"role": "system", "content": "You are a precise academic paper classifier. Only output valid JSON array of strings."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.0,
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()


def infer_categories(papers):
    """Use DeepSeek API to batch-infer category for each paper. Falls back to heuristic if unavailable."""
    if not DEEPSEEK_API_KEY:
        print("  DEEPSEEK_API_KEY not set, using heuristic fallback for categories.")
        return _heuristic_categories(papers)

    BATCH_SIZE = 15
    all_categories = []

    for batch_start in range(0, len(papers), BATCH_SIZE):
        batch = papers[batch_start:batch_start + BATCH_SIZE]
        lines = []
        for i, pub in enumerate(batch):
            lines.append(f"{batch_start + i + 1}. Title: \"{pub['title']}\"\n   Venue: {pub['publication']}")
        prompt = CATEGORY_PROMPT + "\n\n" + "\n".join(lines)

        try:
            content = _call_deepseek(prompt)
            # Strip markdown code fences if present
            if content.startswith("```"):
                content = content.split("\n", 1)[1]
                if content.endswith("```"):
                    content = content[:-3]
            categories = json.loads(content)

            if isinstance(categories, list) and len(categories) == len(batch):
                valid = set(CATEGORY_OPTIONS)
                clean = [c if c in valid else "期刊论文" for c in categories]
                all_categories.extend(clean)
                print(f"  LLM batch {batch_start // BATCH_SIZE + 1}: {len(batch)} papers classified.")
                continue
            else:
                raise ValueError(f"Expected {len(batch)} categories, got {len(categories) if isinstance(categories, list) else type(categories)}")

        except Exception as e:
            print(f"  LLM batch {batch_start // BATCH_SIZE + 1} failed ({e}), using heuristic for this batch.")
            all_categories.extend(_heuristic_categories(batch))

    return all_categories


def _heuristic_categories(papers):
    """Rule-based category inference as fallback."""
    results = []
    for pub in papers:
        title_lower = pub["title"].lower()
        venue_lower = pub["publication"].lower() if pub["publication"] else ""

        if any(kw in title_lower for kw in ["survey", "review", "综述"]):
            results.append("综述论文")
            continue

        if venue_lower:
            conf_kw = ["conference", "proceedings", "cec", "gecco", "ivcnz", "ssci",
                       "symposium", "workshop", "congress", "iceaai"]
            if any(kw in venue_lower for kw in conf_kw):
                results.append("会议论文")
                continue

        results.append("期刊论文")
    return results


def save_pubs(pubs):
    """Save publications to YAML, sorted by year descending."""
    # Remove cited_by from output (it was just for reference)
    for pub in pubs:
        pub.pop("cited_by", None)

    pubs.sort(key=lambda x: x.get("year", 0), reverse=True)

    PUBLICATIONS_FILE.parent.mkdir(parents=True, exist_ok=True)

    output = ""
    for i, pub in enumerate(pubs):
        if i > 0:
            output += "\n"
        output += f"- authors: {yaml.dump(pub.get('authors', []), allow_unicode=True, default_flow_style=True).strip()}\n"
        output += f"  title: {yaml.dump(pub.get('title', ''), allow_unicode=True).strip()}\n"

        venue = pub.get("publication") or pub.get("publisher") or ""
        output += f"  publication: {yaml.dump(venue, allow_unicode=True).strip()}\n"
        output += f"  year: {pub.get('year', 0)}\n"
        output += f"  url_custom: {yaml.dump(pub.get('url_custom', ''), allow_unicode=True).strip()}\n"
        output += f"  category: {yaml.dump(pub.get('category', '期刊论文'), allow_unicode=True).strip()}\n"

        for key in ["doi", "tags", "url_pdf", "url_code", "volume", "pages", "note"]:
            if key in pub and pub[key]:
                output += f"  {key}: {yaml.dump(pub[key], allow_unicode=True, default_flow_style=True).strip()}\n"

    with open(PUBLICATIONS_FILE, "w", encoding="utf-8") as f:
        f.write(output)


def main():
    if not SERPAPI_API_KEY:
        print("Error: SERPAPI_API_KEY environment variable not set.")
        print("Usage: SERPAPI_API_KEY=xxx [DEEPSEEK_API_KEY=xxx] python scripts/sync_publications.py")
        sys.exit(1)

    print("Fetching articles from Google Scholar (SerpAPI)...")
    articles = fetch_all_articles()
    print(f"Total articles fetched: {len(articles)}\n")

    print("Loading existing publications...")
    existing_pubs = load_existing_pubs()
    print(f"Existing publications: {len(existing_pubs)}\n")

    if not articles:
        print("No articles fetched. Check API key and author ID.")
        sys.exit(1)

    # Collect new papers
    new_papers = []
    for article in articles:
        if is_duplicate(article, existing_pubs):
            continue
        pub = map_article_to_pub(article)
        new_papers.append(pub)
        existing_pubs.append(pub)

    if not new_papers:
        print("No new publications found. Data is up to date.")
        return

    # Infer categories for new papers
    print(f"Inferring categories for {len(new_papers)} new papers...")
    categories = infer_categories(new_papers)
    for pub, cat in zip(new_papers, categories):
        pub["category"] = cat
        title_short = pub["title"][:80] + ("..." if len(pub["title"]) > 80 else "")
        print(f"  [{pub['year']}] [{cat}] {title_short}")

    print(f"\n{len(new_papers)} new publications added. Saving to {PUBLICATIONS_FILE}...")
    save_pubs(existing_pubs)
    print("Done.")


if __name__ == "__main__":
    main()
