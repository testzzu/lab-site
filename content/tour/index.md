---
title: 主页
date: 2022-10-24

type: landing

sections:
  - block: slider
    content:
      slides:
      - title: 👋 欢迎来到实验室
        content: 了解我们的研究工作...
        align: center
        background:
          image:
            filename: coders.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: 🔬 进化智能与感知学习
        content: 专注于前沿的人工智能研究
        align: center
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: 📚 学术研究
        content: 探索智能计算的新领域
        align: center
        background:
          image:
            filename: contact.jpg
            filters:
              brightness: 0.7
          position: left
          color: '#444'

  - block: features
    content:
      title: 研究领域
      subtitle: 我们的主要研究方向
      items:
        - name: 进化计算
          description: 基于生物进化原理的智能优化算法
          icon: dna
          icon_pack: fas
        - name: 机器学习
          description: 深度学习与神经网络技术
          icon: brain
          icon_pack: fas
        - name: 感知学习
          description: 多模态感知与认知学习
          icon: eye
          icon_pack: fas

  - block: collection
    content:
      title: 最新动态
      subtitle: 实验室最新消息
      text: 了解我们的最新研究成果和活动
      filters:
        folders:
          - post
        featured_only: true
        limit: 3
      design:
        columns: '1'
        view: card
        flip_alt_rows: false

  - block: collection
    content:
      title: 团队成员
      subtitle: 认识我们的研究团队
      text: 优秀的教师和研究生团队
      filters:
        folders:
          - authors
        featured_only: true
        limit: 4
      design:
        columns: '2'
        view: card
        flip_alt_rows: false

  - block: contact
    content:
      title: 联系我们
      subtitle: 欢迎与我们交流
      text: 如果您对我们的研究感兴趣，欢迎联系我们
      email: ywang@zzudu.cn
      address:
        street: 科学大道100号
        city: 郑州市
        region: 河南省
        postcode: 450001
        country: 中国
        country_code: CN
      phone: ''
      contact_links:
        - icon: envelope
          icon_pack: fas
          name: 发送邮件
          link: 'mailto:ywang@zzudu.cn'
      coordinates:
        latitude: '34.7566'
        longitude: '113.6409'
      zoom: 15
      directions: 电气与信息工程学院
      office_hours:
        - '周一至周五 9:00-17:00'
      appointment_url: 'mailto:ywang@zzudu.cn'
---
