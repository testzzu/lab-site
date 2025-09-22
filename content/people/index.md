---
title: People
date: 2022-10-24

type: landing

sections:
  - block: people
    content:
      title: 研究团队
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - 团队负责人
          - 博士研究生
          - 硕士研究生
          - 科研助理
      sort_by: Params.enroll_date
      sort_ascending: true
    design:
      show_interests: true
      show_role: true
      show_social: true
  - block: markdown
    content:
      title: 已毕业研究生
      text: |
        - 连锦涛（硕士研究生）：基于遗传规划的医学图像分类
        - 李文静（硕士研究生）：基于遗传规划的符号回归
        - 杨泽轩（硕士研究生）：基于遗传规划遥感图像分类
        - 道明扬（硕士研究生）：面向高位数据分类的多树遗传规划特征构建方法研究
        - 李阳光（硕士研究生）：基于进化集成学习算法的电机故障诊断方法研究
        - 刘艮跃（硕士研究生）：进化神经架构搜索
---

<script>
// 自定义JavaScript：让people页面的名字点击跳转到GitHub
document.addEventListener('DOMContentLoaded', function() {
  // 查找所有人员卡片中的名字链接
  const nameLinks = document.querySelectorAll('.portrait-title h2 a');
  
  nameLinks.forEach(function(nameLink) {
    // 找到对应的社交链接区域
    const card = nameLink.closest('.portrait-title').parentElement;
    const socialLinks = card.querySelectorAll('.network-icon a');
    
    let githubLink = null;
    
    // 查找GitHub链接
    socialLinks.forEach(function(socialLink) {
      if (socialLink.getAttribute('href') && socialLink.getAttribute('href').includes('github.com')) {
        githubLink = socialLink.getAttribute('href');
      }
    });
    
    // 如果找到GitHub链接，修改名字链接
    if (githubLink) {
      nameLink.setAttribute('href', githubLink);
      nameLink.setAttribute('target', '_blank');
      nameLink.setAttribute('rel', 'noopener');
      nameLink.setAttribute('title', '查看GitHub主页');
      
      // 添加GitHub图标提示
      nameLink.style.position = 'relative';
      nameLink.innerHTML = nameLink.innerHTML + ' <i class="fab fa-github" style="font-size: 0.8em; margin-left: 5px;"></i>';
    }
  });
});
</script>

<style>
/* 自定义样式：美化GitHub链接 */
.portrait-title h2 a:hover {
  color: #007bff !important;
  text-decoration: underline !important;
}

.portrait-title h2 a i.fa-github {
  opacity: 0.7;
  transition: opacity 0.3s ease;
}

.portrait-title h2 a:hover i.fa-github {
  opacity: 1;
}
</style>