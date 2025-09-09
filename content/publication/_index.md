---
title: 出版物

# Listing view
view: citation

# Optional banner image (relative to `assets/media/` folder).
banner:
  caption: ''
  image: ''

# 配置出版物直接跳转到外部链接
publication_types:
  - 0  # 所有类型都直接跳转
  
# 确保分区列表页被渲染
build:
  list: always

# 关闭该分区内每篇出版物的详情页渲染，仅保留列表页
cascade:
  build:
    render: never
    list: always
    publishResources: true
---
