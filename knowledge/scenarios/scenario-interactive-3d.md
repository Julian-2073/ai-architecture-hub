> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 旋转查看产品或空间场景

ID：`scenario-interactive-3d`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

产品 / 模型 / 物体 / 场景 / 展厅 / 空间 / 3d / 三维；旋转 / 转动 / 拖动 / 交互 / 展示 / 查看 / 模拟。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

资产制作与运行渲染分开；只选择适合目标平台的一种主要运行路线，仿真计算独立判断。

- 已有模型资产还是要制作？
- 仅展示还是有真实物理或业务模拟？

## 技术职责与候选

- [Three.js](../technologies/tech-threejs.md)：浏览器运行渲染候选
- [Babylon.js](../technologies/tech-babylonjs.md)：浏览器场景引擎候选
- [Blender](../technologies/tech-blender.md)：制作和导出模型资产
- [Godot](../technologies/tech-godot.md)：独立场景运行路线候选

## 模块与数据流

资产制作与导出 → 场景加载 → 业务状态 → 交互与渲染。

## 实现后应观察

- 目标设备操作与帧率满足要求
- 资产单位、体积和授权明确

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-interactive-3d.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 口语发现补充（2026-10-17）

支持“转着看、换颜色、走进厂里画面”等发现线索；多义说法仍由Codex解释和确认。实现步骤见[产品三维路径](../templates/template-path-product-3d.md)。[社区版来源登记](../../evidence/curation/scenario-interactive-3d.json)。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-interactive-3d.json)。
