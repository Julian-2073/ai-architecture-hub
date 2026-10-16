> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 保存记录并能查询修改

ID：`scenario-database-persistence`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

记录 / 订单 / 客户 / 数据；保存 / 持久化 / 查询 / 修改 / 事务 / 数据库。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 关系、约束和并发写要求是什么？
- 现有数据库和恢复目标是什么？

## 技术职责与候选

- [PostgreSQL](../technologies/tech-postgresql.md)：事务、结构化存储和 SQL 查询。
- [SQLite](../technologies/tech-sqlite.md)：单文件、本地 SQL 存储。
- [MongoDB](../technologies/tech-mongodb.md)：用文档模型存储和查询数据。

## 模块与数据流

业务数据 → schema与约束 → 事务 → 查询 → 备份恢复。

## 实现后应观察

- 关键约束与事务正确
- 备份可恢复

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-database-persistence.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-database-persistence.json)。
