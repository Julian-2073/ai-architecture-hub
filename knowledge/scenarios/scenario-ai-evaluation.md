> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 比较AI回答和工具行为

ID：`scenario-ai-evaluation`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

AI / ai / 模型 / 智能体 / 回答；评估 / 比较 / 质量 / 准确 / 幻觉 / 回归。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 人工标准和代表性样本是什么？
- 正确性、成本、引用与工具动作如何分别评判？

## 技术职责与候选

- [promptfoo](../technologies/tech-promptfoo.md)：批量比较提示与模型输出并运行检查。
- [Ragas](../technologies/tech-ragas.md)：组织检索和生成任务的评估指标。
- [LangSmith](../technologies/tech-langsmith.md)：追踪模型应用并组织评估。

## 模块与数据流

样本与标签 → 任务执行 → 断言与判分 → 失败分析。

## 实现后应观察

- 人工与自动标准校准
- 结果可复现且费用明确

## 可选模板

- [最小技术验证 PoC](../templates/template-poc.md)
- [项目集成验收](../templates/template-acceptance.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-ai-evaluation.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-ai-evaluation.json)。
