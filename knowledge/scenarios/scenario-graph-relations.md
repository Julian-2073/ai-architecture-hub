> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 沿复杂关系寻找路径

ID：`scenario-graph-relations`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

关系 / 实体 / 客户 / 企业 / 知识图谱；几层 / 多跳 / 路径 / 关联查询 / 找关系。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 典型查询路径是什么？
- 关系表和索引为什么不能满足？

## 技术职责与候选

- [Neo4j](../technologies/tech-neo4j.md)：存储节点关系并进行图查询。
- [PostgreSQL](../technologies/tech-postgresql.md)：事务、结构化存储和 SQL 查询。

## 模块与数据流

实体与关系 → 存储建模 → 路径查询 → 解释。

## 实现后应观察

- 关键路径查询准确
- 同数据比较关系库方案

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-graph-relations.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 本轮选型与组合分界

[按业务问题选择搜索路线](../capabilities/cap-domain-search.md)；使用[搜索质量与同步模板](../templates/template-search-quality.md)对照同一查询集。精确查找先复用业务接口，相关性/语义/图路径按缺口再比较；候选不要求全部安装。

[社区版来源登记](../../evidence/curation/scenario-graph-relations.json)为inference，没有项目运行通过结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-graph-relations.json)。
