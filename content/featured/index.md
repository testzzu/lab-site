---
# 标题
title: 代表性工作
summary: 展示团队的代表性研究成果与重要论文。
date: 2025-09-11
# Hugo section type
# Use page bundle to render as a list/collection page
# You can customize layout via layouts/section/publication.html if needed

# 页面类型（可保留为默认）
type: page

# 将此页面加入站点地图
sitemap:
  priority: 0.6

# 页面内容块
sections:
  - block: collection
    content:
      title: 代表性工作
      text: 我们精选了部分具有代表性的工作与论文。
      count: 20
      filters:
        # 仅展示被标记为 featured 的 publication
        folders:
          - publication
        featured_only: true
      # 排序：按日期降序
      offset: 0
      order: desc
      page_type: publication
    design:
      view: citation
      columns: '1'
---
