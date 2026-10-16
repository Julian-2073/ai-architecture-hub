> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 图网络、二维画布、布局与动画

## 从业务描述开始

要探索关系、编辑图形、计算布局，还是播放动画？

## 能力接口

图结构/场景/动画资产 → 交互画面与布局结果。这是职责示意，不是固定API。

## 情境化决策分支

1. 关系探索：把图结构、图分析和渲染层分开。
2. 节点流程编辑：编辑器与执行器分离；布局库只计算位置。
3. 图片/形状编辑：评估对象模型、撤销、序列化和导出，不以能拖动等同完整编辑器。
4. 动画：区分资产播放与代码时间线，验证特效、性能和减少动态效果。

## 候选与关系

- [Cytoscape.js](../technologies/tech-cytoscape.md)：展示并操作节点关系网络。
- [Sigma.js](../technologies/tech-sigma.md)：显示和交互较大关系网络。
- [Graphology](../technologies/tech-graphology.md)：组织图结构与相关算法能力。
- [ELK.js](../technologies/tech-elkjs.md)：为节点边计算布局位置。
- [Dagre](../technologies/tech-dagre.md)：计算分层图的节点和边布局。
- [PixiJS](../technologies/tech-pixijs.md)：组织高交互二维图形与精灵渲染。
- [Konva](../technologies/tech-konva.md)：组织形状、图层、事件与交互。
- [Fabric.js](../technologies/tech-fabric.md)：提供对象化图形交互与序列化。
- [Lottie Web](../technologies/tech-lottie.md)：在Web播放受支持的动画描述。
- [GSAP](../technologies/tech-gsap.md)：编排时间线和界面动画。
- [Motion](../technologies/tech-motion.md)：实现交互与布局等界面动画。

## 关键验证与退出

核查：真实图规模、标签、密集布局、输入法、触控、导出与GPU。

保留：节点边、形状与文档模型、原始资产、布局和动画配置。

[情境决策树模板](../templates/template-selection-decision-tree.md)、[完整地图](cap-software-map.md)。建议来自 [社区版来源登记](../../evidence/curation/cap-domain-advanced-graphics.json)，没有执行候选软件或项目验收。

## 节点编辑的组合关系

[React Flow](../technologies/tech-react-flow.md)可承担节点画布、连线与选择；布局、图查询与执行语义分别判断，参见[关系图组合指南](cap-solution-relationship-workbench.md)。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-advanced-graphics.json)。
