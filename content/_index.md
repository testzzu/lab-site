---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        # 进化智能与感知学习实验室
        ## Evolution Intelligence & Perception Learning Laboratory
        ### EIPL
      image:
        filename: welcome.jpg
      text: |
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
          <div style="text-align: left;">
            <img src="images/zzu-logo.png" alt="University Logo" style="height: 80px; margin-right: 20px;">
          </div>
          <div style="text-align: right;">
            <img src="images/lab-logo.png" alt="Lab Logo" style="height: 80px;">
          </div>
        </div>
        <br>
        
        The **Evolution Intelligence & Perception Learning Laboratory (EIPL)** has been a center of excellence for Artificial Intelligence research, teaching, and practice since its founding in 2016.
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  - block: markdown
    content:
      title:
      subtitle: '' 
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
