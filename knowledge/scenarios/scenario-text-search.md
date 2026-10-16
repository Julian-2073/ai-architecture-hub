> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 按编号、字段或关键词查找

ID：`scenario-text-search`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

搜索 / 查找 / 查资料 / 搜到；关键词 / 产品 / 目录 / 文档 / 中文 / 全文。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 中文查询和排序标准是什么？
- 数据更新与删除怎样同步？

## 技术职责与候选

- [Meilisearch](../technologies/tech-meilisearch.md)：文本搜索、筛选及相关性配置。
- [Elasticsearch](../technologies/tech-elasticsearch.md)：索引文档并执行全文搜索和聚合。
- [OpenSearch](../technologies/tech-opensearch.md)：提供文档检索、聚合和分析能力。
- [PostgreSQL](../technologies/tech-postgresql.md)：事务、结构化存储和 SQL 查询。

## 模块与数据流

主库 → 索引同步 → 查询与过滤 → 排序 → 结果。

## 实现后应观察

- 真实查询相关性达到标准
- 删除和权限及时生效

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-text-search.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 本轮选型与组合分界

[按业务问题选择搜索路线](../capabilities/cap-domain-search.md)；使用[搜索质量与同步模板](../templates/template-search-quality.md)对照同一查询集。精确查找先复用业务接口，相关性/语义/图路径按缺口再比较；候选不要求全部安装。

[社区版来源登记](../../evidence/curation/scenario-text-search.json)为inference，没有项目运行通过结论。

也可从“按客户编号/订单号查找”进入；Codex应先判断精确记录而非默认全文引擎。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-text-search.json)。
