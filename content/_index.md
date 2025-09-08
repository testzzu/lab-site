---
# Leave the homepage title empty to use the site title
title:
date: 2025-09-07
type: landing

sections:
  - block: markdown
    content:
      title:
      subtitle:
      text: |
        <style>
          /* Fix carousel image height and crop via object-fit */
          #homeCarousel .carousel-item img { height: 420px; width: 100%; object-fit: cover; }
          @media (max-width: 576px) {
            #homeCarousel .carousel-item img { height: 240px; }
          }
        </style>
        <div id="homeCarousel" class="carousel slide" data-ride="carousel" data-interval="4000" style="margin:30px 0 40px 0;">
          <ol class="carousel-indicators">
            <li data-target="#homeCarousel" data-slide-to="0" class="active"></li>
            <li data-target="#homeCarousel" data-slide-to="1"></li>
            <li data-target="#homeCarousel" data-slide-to="2"></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="./media/coders.jpg" class="d-block w-100 border-0" alt="Welcome">
            </div>
            <div class="carousel-item">
              <img src="./media/coders.jpg" class="d-block w-100 border-0" alt="Coders">
            </div>
            <div class="carousel-item">
              <img src="./media/contact.jpg" class="d-block w-100 border-0" alt="Contact">
            </div>
          </div>
          <a class="carousel-control-prev" href="#homeCarousel" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#homeCarousel" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['0', '0', '0', '0']
  - block: hero
    design:
      spacing:
        padding: ['0', '0', '0', '0']
      background:
        color: '#ffffff'
    content:
      title: |
        # 进化智能与感知学习实验室
        ## Evolution Intelligence & Perception Learning Laboratory
        ### EIPL
      image:
        filename: welcome.jpg
      text: |
        
        
        The **Evolution Intelligence & Perception Learning Laboratory (EIPL)** has been a center of excellence for Artificial Intelligence research, teaching, and practice since its founding in 2016.
  
  - block: collection
    content:
      title: 新闻
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
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: '' 
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen

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
