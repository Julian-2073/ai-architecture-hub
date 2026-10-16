> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 多人一起修改同一份文档

ID：`scenario-collaborative-doc`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

几个人 / 多人 / 同时 / 一起 / 协同 / 协作 / collaborative；文档 / 改一份 / 修改 / 编辑 / 写 / document。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先选一种编辑器；确有多人或离线合并需求再组合共享状态层，不同时引入两套编辑器。

- 要保存哪些文档格式？
- 是否需要断网编辑和冲突合并？

## 技术职责与候选

- [Yjs](../technologies/tech-yjs.md)：共享文档同步与合并
- [Tiptap](../technologies/tech-tiptap.md)：富文本编辑器候选，与 Lexical 比较
- [Lexical](../technologies/tech-lexical.md)：富文本编辑器候选，与 Tiptap 比较

## 模块与数据流

编辑器 → 共享文档状态 → 同步与存储 → 权限与历史。

## 实现后应观察

- 并发改动不静默丢失
- 重连和权限边界可验证

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-collaborative-doc.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-collaborative-doc.json)。
