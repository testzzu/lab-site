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
          /* Center the hero section content */
          .hero-centered h1,
          .hero-centered h2,
          .hero-centered h3,
          .hero-centered p { text-align: center; }
          .hero-centered .hero-intro { max-width: 900px; margin-left: auto; margin-right: auto; text-align: center !important; margin-bottom: 36px; }
          .hero-centered .hero-intro p,
          .hero-centered .hero-intro h1,
          .hero-centered .hero-intro h2,
          .hero-centered .hero-intro h3 { text-align: center !important; }
          .hero-centered .row { justify-content: center; }
          .hero-centered .col-md-6 { text-align: center; }
          .hero-centered ul { display: inline-block; text-align: left; }
          .hero-centered .mx-auto { margin-left: auto !important; margin-right: auto !important; }
          .hero-centered .col-12 { text-align: center; }
          .hero-centered .card { text-align: left; }
          /* Center outer hero container */
          .hero-centered .hero-lead { max-width: 1100px; margin-left: auto; margin-right: auto; text-align: center; }
          /* Ensure hero inner content takes full width (no image column reserved) */
          .hero-centered .col-lg-8,
          .hero-centered .col-md-10 { max-width: 100% !important; flex: 0 0 100% !important; margin-left: auto; margin-right: auto; }
          @media (min-width: 1200px) {
            .hero-centered .mx-auto { max-width: 1100px; }
          }
          /* Academic aesthetic helpers */
          .hero-centered .section-title { font-weight: 700; letter-spacing: .3px; margin: 10px 0 16px; }
          .hero-centered .section-title .accent { display: inline-block; height: 3px; width: 44px; background: linear-gradient(90deg, #1d6ef0, #6bc1ff); border-radius: 2px; margin-top: 6px; }
          .hero-centered .feature-list { list-style: none; padding-left: 0; margin-bottom: 0; }
          .hero-centered .feature-list li { margin: 8px 0; font-size: 0.95rem; }
          .hero-centered .feature-list li i { color: #1d6ef0; margin-right: 8px; }
          .hero-centered .subtle-card { background: #fafbff; border: 1px solid #eef2ff; border-radius: 12px; padding: 18px; text-align: left; height: 100%; width: 100%; }
          .hero-centered .pill { display: inline-block; font-size: 12px; background: #eef4ff; color: #2d5be3; padding: 2px 8px; border-radius: 999px; margin-left: 6px; vertical-align: middle; }
          /* Meta section (bottom three cards) */
          .hero-centered .meta-card { background: #fcfcfe; border: 1px solid #eef2ff; border-radius: 12px; padding: 16px 18px; text-align: left; height: 100%; }
          .hero-centered .meta-title { font-size: 1.05rem; font-weight: 600; margin: 0; }
          .hero-centered .meta-text { font-size: 0.95rem; color: #50555e; margin-bottom: 0; text-align: left; }
          .hero-centered .meta-head { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
          .hero-centered .meta-icon { width: 22px; text-align: center; color: #2d5be3; margin-right: 6px; }
          .hero-centered .equalize-row-3 > [class^="col-"] { display: flex; }
          /* Equal height cards for project showcase */
          .hero-centered .equalize-row-cards > [class^="col-"] { display: flex; }
          .hero-centered .equalize-row-cards .card { height: 100%; width: 100%; }
          /* Equal height helpers for hero two-column cards */
          .hero-centered .equalize-row > [class^="col-"] { display: flex; }
        </style>
        <div id="homeCarousel" class="carousel slide" data-ride="carousel" data-interval="4000" style="margin:30px 0 40px 0;">
          <ol class="carousel-indicators">
            <li data-target="#homeCarousel" data-slide-to="0" class="active"></li>
            <li data-target="#homeCarousel" data-slide-to="1"></li>
            <li data-target="#homeCarousel" data-slide-to="2"></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="./media/team.jpg" class="d-block w-100 border-0" alt="Team">
            </div>
            <div class="carousel-item">
              <img src="./media/team3.jpg" class="d-block w-100 border-0" alt="Coders">
            </div>
            <div class="carousel-item">
              <img src="./media/team2.jpg" class="d-block w-100 border-0" alt="Contact">
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
      columns: '1'
      css_class: hero-centered
    content:
      align: center
      title: |
        # 进化智能与感知学习团队
        ## Evolutionary Intelligence and Perception Learning Laboratory (EIPL)
      text: |
        <div class="hero-lead">
        <div class="hero-intro">
          <h3 class="section-title">研究简介<div class="accent"></div></h3>
          <p class="lead" style="font-weight: 500; color: #2b2f36;">进化智能与感知学习组（EIPL Group）是一个跨学科研究团队，专注于探索人工智能的前沿领域。我们以自然进化法则为灵感，致力于研究具备主动感知、持续学习和自主进化能力的新一代智能算法。我们的研究重点涵盖计算机视觉、进化计算、机器学习和特征工程等领域。</p>
        </div>
        
        <div class="text-center" style="margin-bottom: 40px;">
          <img src="./media/EIPL.png" alt="EIPL Lab" style="width: 100%; height: auto; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border-radius: 12px;">
        </div>

        <div class="mx-auto" style="max-width: 1100px;">
        <div class="row justify-content-center equalize-row">
          <div class="col-md-6 text-center">
            <div class="subtle-card">
              <h4 style="margin-bottom: 10px;">核心研究方向<span class="pill">Focus</span></h4>
              <ul class="feature-list">
                <li><i class="fas fa-circle"></i><strong>计算机视觉</strong>：图像理解、目标检测与分割、三维视觉</li>
                <li><i class="fas fa-circle"></i><strong>进化计算</strong>：遗传规划、群体智能、代理辅助与多目标优化</li>
                <li><i class="fas fa-circle"></i><strong>机器学习</strong>：深度学习、强化学习、迁移与小样本学习</li>
                <li><i class="fas fa-circle"></i><strong>特征工程</strong>：自监督表征、可解释表示与结构先验</li>
              </ul>
            </div>
          </div>
          <div class="col-md-6 text-center">
            <div class="subtle-card">
              <h4 style="margin-bottom: 10px;">应用场景与成果<span class="pill">Impact</span></h4>
              <ul class="feature-list">
                <li><i class="fas fa-check"></i>医疗影像分析</li>
                <li><i class="fas fa-check"></i>辅助诊断</li>
                <li><i class="fas fa-check"></i>精准农业</li>
                <li><i class="fas fa-check"></i>智能育种与表型分析</li>
                <li><i class="fas fa-check"></i>病虫害监测</li>
              </ul>
            </div>
          </div>
        </div>
        
        <div class="row mt-4 justify-content-center">
          <div class="col-12">
            <h4>技术特色与创新</h4>
            <div class="row justify-content-center">
              <div class="col-md-3">
                <div class="text-center p-3">
                  <i class="fas fa-cogs fa-2x text-primary mb-2"></i>
                  <h6>多技术融合</h6>
                  <small class="text-muted">CV+ML+EC</small>
                </div>
              </div>
              <div class="col-md-3">
                <div class="text-center p-3">
                  <i class="fas fa-brain fa-2x text-success mb-2"></i>
                  <h6>小样本学习</h6>
                  <small class="text-muted">Few-Shot Learning</small>
                </div>
              </div>
              <div class="col-md-3">
                <div class="text-center p-3">
                  <i class="fas fa-robot fa-2x text-warning mb-2"></i>
                  <h6>自动化机器学习</h6>
                  <small class="text-muted">AutoML</small>
                </div>
              </div>
              <div class="col-md-3">
                <div class="text-center p-3">
                  <i class="fas fa-eye fa-2x text-info mb-2"></i>
                  <h6>可解释AI</h6>
                  <small class="text-muted">XAI</small>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="row mt-4 justify-content-center equalize-row-cards">
          <div class="col-md-4">
            <div class="card mb-3">
              <img src="./media/homepage/jaffe.png" class="card-img-top" alt="进化算法优化" style="height: 200px; object-fit: cover;">
              <div class="card-body">
                <h6 class="card-title">进化算法优化</h6>
                <p class="card-text small">我们致力于进化计算的前沿研究，涵盖遗传规划（GP）等多种进化算法。研究重点包括多目标优化、自动特征工程与自适应模型构建，并广泛应用于图像分类、遥感解译与医学影像分析等领域。</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card mb-3">
              <img src="./media/homepage/skincancer.png" class="card-img-top" alt="医疗影像AI分析" style="height: 200px; object-fit: cover;">
              <div class="card-body">
                <h6 class="card-title">医疗影像AI分析</h6>
                <p class="card-text small">现有计算机辅助诊断（CAD）系统存在局限：传统方法依赖领域知识提取特征，神经网络方法需专业设计网络结构且可解释性差。该方法性能多数优于基于GP、神经网络特征学习及传统对比方法，且演化出的模型树结构更小，具有潜在高可解释性。</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card mb-3">
              <img src="./media/WHU.png" class="card-img-top" alt="农业领域" style="height: 200px; object-fit: cover;">
              <div class="card-body">
                <h6 class="card-title">农业领域-场景识别</h6>
                <p class="card-text small">针对现有作物分类特征构建方法依赖领域知识且解可解释性不足的问题，提出了一种基于多树遗传编程（GP）的新方法，旨在自动演化高可解释性的解，从高光谱图像中构建用于作物分类的高层特征。</p>
              </div>
            </div>
          </div>

        </div>
        
        <div class="row mt-4 justify-content-center">
          <div class="col-lg-8">
            <div class="row">
              <div class="col-md-6">
                <div class="meta-card">
                  <div class="meta-head">
                    <span class="meta-icon"><i class="fas fa-users"></i></span>
                    <h5 class="meta-title">团队介绍</h5>
                  </div>
                  <p class="meta-text">专注于计算机视觉、进化计算、机器学习与特征工程等前沿领域的交叉研究，致力于推动人工智能技术的创新与应用。</p>
                </div>
              </div>
              <div class="col-md-6">
                <div class="meta-card">
                  <div class="meta-head">
                    <span class="meta-icon"><i class="fas fa-envelope"></i></span>
                    <h5 class="meta-title">联系方式</h5>
                  </div>
                  <p class="meta-text">
                    <strong>团队负责人：</strong>毕莹教授<br>
                    <strong>邮箱：</strong>yingbi[at]zzu.edu.cn<br>
                    <strong>地址：</strong>河南省郑州市科学大道100号
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        </div>
        </div>
  
  - block: collection
    content:
      title: 课题组动态
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

  # - block: collection
  #   content:
  #     title: 最新工作
  #     text: ""
  #     count: 5
  #     filters:
  #       page_type: publication
  #       publication_type: ''
  #       exclude_featured: false
  #     offset: 0
  #     order: desc
  #   design:
  #     view: citation
  #     columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="研究团队 →" %}}
    design:
      columns: '1'
---
