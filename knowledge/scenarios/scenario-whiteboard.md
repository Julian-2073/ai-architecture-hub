> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 自由画图并移动图形

ID：`scenario-whiteboard`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

白板 / 画布 / 草图 / 手绘 / 画图 / 绘图；拖动 / 自由 / 图形 / 协作 / 连线 / 绘制 / 画。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 自由绘图还是结构化流程图？
- 需要导出、多人编辑或历史吗？

## 技术职责与候选

- [tldraw](../technologies/tech-tldraw.md)：嵌入可扩展的绘图与白板交互。
- [Excalidraw](../technologies/tech-excalidraw.md)：绘制图形、关系示意与白板内容。

## 模块与数据流

图形状态 → 画布交互 → 文档存储 → 可选协同。

## 实现后应观察

- 图形和位置可恢复
- 中文与导出格式正确

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-whiteboard.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-whiteboard.json)。
