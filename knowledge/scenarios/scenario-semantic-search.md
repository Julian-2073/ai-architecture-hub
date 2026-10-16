> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 表达不同也能找到同一意思

ID：`scenario-semantic-search`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

意思 / 语义 / 相似 / 同义 / 换个说法；找 / 搜 / 检索 / 资料 / 匹配。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 关键词检索为何不够？
- 有可标注查询、过滤和领域要求吗？

## 技术职责与候选

- [pgvector](../technologies/tech-pgvector.md)：在数据库内保存和检索向量。
- [Qdrant](../technologies/tech-qdrant.md)：向量相似度检索与元数据过滤。
- [Sentence Transformers](../technologies/tech-sentence-transformers.md)：生成语义向量或训练相关模型。

## 模块与数据流

文本 → 嵌入 → 向量索引 → 权限过滤 → 检索评估。

## 实现后应观察

- 与关键词基线比较召回
- 换模型与删除后索引可重建

## 可选模板

- [需求与约束记录](../templates/template-requirements.md)
- [技术方案成本估算模型](../templates/template-cost-model.md)
- [最小技术验证 PoC](../templates/template-poc.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-semantic-search.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 本轮选型与组合分界

[按业务问题选择搜索路线](../capabilities/cap-domain-search.md)；使用[搜索质量与同步模板](../templates/template-search-quality.md)对照同一查询集。精确查找先复用业务接口，相关性/语义/图路径按缺口再比较；候选不要求全部安装。

[社区版来源登记](../../evidence/curation/scenario-semantic-search.json)为inference，没有项目运行通过结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-semantic-search.json)。
