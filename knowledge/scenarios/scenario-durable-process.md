> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 长时间流程失败后继续执行

ID：`scenario-durable-process`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

流程 / 任务 / 订单 / 步骤；几天 / 长时间 / 断点 / 恢复 / 继续执行 / 跨服务。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 需要保留哪些状态和人工节点？
- 外部动作如何幂等和补偿？

## 技术职责与候选

- [Temporal](../technologies/tech-temporal.md)：在故障后继续长时运行的工作流。
- [LangGraph](../technologies/tech-langgraph.md)：组织状态、节点、分支与持久化执行。

## 模块与数据流

状态机 → 持久化执行 → Worker → 恢复与补偿 → 审计。

## 实现后应观察

- 故障后从正确位置恢复
- 重复执行与版本升级可控

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-durable-process.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-durable-process.json)。
