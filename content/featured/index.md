---
# 标题
title: 代表性工作
summary: 展示团队的代表性研究成果与重要论文。
date: 2025-09-11
# Hugo section type
# Use page bundle to render as a list/collection page
# You can customize layout via layouts/section/publication.html if needed

# 页面类型：使用 landing 以启用 sections 小部件渲染
type: landing

# 将此页面加入站点地图
sitemap:
  priority: 0.6

# 页面内容块
sections:
  - block: collection
    content:
      count: 20
      filters:
        folders:
          - publication
        featured_only: true
        featured_only: true
      # 排序：按日期降序
      offset: 0
      order: desc
      page_type: publication
    design:
      view: card
      columns: '4'
---
