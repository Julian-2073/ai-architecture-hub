> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 把应用部署并可更新回退

ID：`scenario-release-deploy`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

应用 / 软件 / 服务 / 系统 / 网站；部署 / 上线 / 发布 / 服务器 / 更新回退。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 目标平台、地区和网络是什么？
- 运行、秘密、持久存储和发布授权是什么？

## 技术职责与候选

- [Docker](../technologies/tech-docker.md)：打包应用运行环境和依赖。
- [Caddy](../technologies/tech-caddy.md)：组织 HTTP 服务并管理 HTTPS。
- [GitHub Actions](../technologies/tech-github-actions.md)：根据仓库事件执行构建测试与自动化。所列仓库是 Runner 实现，不是托管服务套餐与权限规则的完整依据；费用、保留时间及工作流权限需查对应服务文档。

## 模块与数据流

构建 → 配置与秘密 → 目标运行 → 健康检查 → 回退。

## 实现后应观察

- 真实入口可用
- 更新、数据与回退可验证

## 可选模板

- [版本兼容与许可核查](../templates/template-compatibility.md)
- [迁移切换与回退](../templates/template-migration.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-release-deploy.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-release-deploy.json)。
