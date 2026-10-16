> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 从客户或公司资料回答并给出处

ID：`scenario-rag-answers`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

资料 / 文档 / 知识库 / 客户材料 / 文件；问一句 / 回答 / 问答 / 出处 / 引用 / 问它 / 提问。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 资料来自哪里，允许传到哪里？
- 哪些人能看哪些资料？

## 技术职责与候选

- [LlamaIndex](../technologies/tech-llamaindex.md)：组织文档接入、索引和检索应用。
- [pgvector](../technologies/tech-pgvector.md)：在数据库内保存和检索向量。
- [Sentence Transformers](../technologies/tech-sentence-transformers.md)：生成语义向量或训练相关模型。

## 模块与数据流

资料接入 → 解析与权限 → 检索 → 回答 → 可回读引用。

## 实现后应观察

- 引用能支持答案
- 无依据和越权问题得到正确处理

## 可选模板

- [需求与约束记录](../templates/template-requirements.md)
- [技术方案成本估算模型](../templates/template-cost-model.md)
- [最小技术验证 PoC](../templates/template-poc.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-rag-answers.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-rag-answers.json)。
