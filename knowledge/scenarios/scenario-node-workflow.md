> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 把几个处理步骤拖动连起来

ID：`scenario-node-workflow`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

拖来拖去 / 搭积木 / 拖拽 / 拖动 / 节点 / 连线 / drag；步骤 / 流程 / 连起来 / 接起来 / 串起来 / workflow。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先明确只画流程还是执行流程；画布与执行器是不同职责，执行器之间另作比较。

- 只画流程还是需要真正执行？
- 步骤由谁配置，失败后怎样处理？

## 技术职责与候选

- [React Flow](../technologies/tech-react-flow.md)：画布与节点连线 UI；不是执行器
- [n8n](../technologies/tech-n8n.md)：业务连接与自动化执行候选
- [LangGraph](../technologies/tech-langgraph.md)：有状态 Agent 执行候选

## 模块与数据流

节点编辑 → 结构校验 → 流程存储 → 可选执行器 → 状态回读。

## 实现后应观察

- 节点与连线可保存恢复
- 执行语义与画布分开验证

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-node-workflow.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-node-workflow.json)。
