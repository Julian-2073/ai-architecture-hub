> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 自动流程中由人确认关键动作

ID：`scenario-human-approval`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

人 / 人工 / 负责人 / 审批人；确认 / 审批 / 审核 / 批准 / 介入。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 谁能审批什么，授权边界在哪里？
- 超时、撤销和重复审批怎样处理？

## 技术职责与候选

- [LangGraph](../technologies/tech-langgraph.md)：组织状态、节点、分支与持久化执行。
- [n8n](../technologies/tech-n8n.md)：连接业务系统并编排触发与动作。
- [Temporal](../technologies/tech-temporal.md)：在故障后继续长时运行的工作流。

## 模块与数据流

草稿或工具计划 → 授权审核 → 受控动作 → 结果与审计。

## 实现后应观察

- 未批准动作不执行
- 批准后可回读且重复请求幂等

## 可选模板

- [需求与约束记录](../templates/template-requirements.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-human-approval.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-human-approval.json)。
