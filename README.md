# 进化智能与感知学习团队 (EIPL)

[biyinglab.org](https://biyinglab.org/)

## 研究方向

- **计算机视觉**：图像理解、目标检测与分割、三维视觉
- **进化计算**：遗传规划、群体智能、代理辅助与多目标优化
- **机器学习**：深度学习、强化学习、迁移与小样本学习
- **特征工程**：自监督表征、可解释表示与结构先验

## 应用场景

医疗影像分析、辅助诊断、精准农业、智能育种与表型分析、病虫害监测、智能调度、智慧电网等。

## 网站内容

本网站基于 [Hugo](https://gohugo.io/) 和 [Wowchemy](https://hugoblox.com/) 研究组模板构建，包含以下版块：

- **主页** — 团队概览、研究方向、技术特色与代表性成果展示
- **团队** — 团队负责人、博士/硕士研究生、科研助理及已毕业研究生信息
- **论文** — 学术出版物列表
- **课题组动态** — 学术会议、论文接收等新闻动态
- **代表性工作** — 精选研究成果展示
- **应用系统** — 课题组应用系统与工程原型（如多机器人协同调度等）
- **相关链接** — 合作实验室与机构链接
- **联系我们** — 研究方向、招生与合作信息

## 本地开发

```bash
# 安装 Hugo (extended 版本)
# 参考: https://gohugo.io/installation/

# 启动开发服务器
hugo server

# 构建静态站点
hugo
```

构建输出位于 `public/` 目录。

## 部署

站点通过 GitHub Pages 部署，域名 [biyinglab.org](https://biyinglab.org/)。推送至 `main` 分支后自动触发构建与部署。

## 目录结构

```
content/          # 网站内容 (Markdown)
  _index.md       # 首页
  people/         # 团队成员
  publication/    # 出版物
  post/           # 课题组动态
  featured/       # 代表性工作
  systems/        # 应用系统
  links/          # 相关链接
  contact/        # 联系我们
  authors/        # 成员个人资料
config/           # Hugo 配置
assets/           # 资源文件
static/           # 静态文件 (图片等)
layouts/          # 自定义布局模板
```

## 许可证

本项目基于 Wowchemy 研究组模板构建，遵循其原始许可。
