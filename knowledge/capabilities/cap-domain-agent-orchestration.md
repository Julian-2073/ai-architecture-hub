> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# AI 应用与 Agent

ID：`cap-domain-agent-orchestration`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

任务/资料/工具结果 → 状态化执行、检索或流程画布。

## 关键判断

工具授权、状态恢复、引用、权限和外部动作幂等。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [LangGraph](../technologies/tech-langgraph.md)
- [LlamaIndex](../technologies/tech-llamaindex.md)
- 可组合的界面层：[React Flow](../technologies/tech-react-flow.md)，提供画布交互，不承担Agent执行。

## 退出与数据

提示、schema、状态、工具接口、资料与执行记录。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-agent-orchestration.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想让AI看资料、调用工具并完成多步任务。

1. **起点**：单次回答能否完成，是否真的需要状态与恢复？
2. **简单或既有路线**：先复用简单调用和工具契约，不默认多Agent。
3. **升级条件**：检索、长期状态、分支或人工介入有需求再选择相应框架。
4. **验证重点**：资料权限、引用、工具副作用、幂等和失败恢复。

[对应模板](../templates/template-ai-tool-contract.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-agent-orchestration.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-agent-orchestration.json)。
