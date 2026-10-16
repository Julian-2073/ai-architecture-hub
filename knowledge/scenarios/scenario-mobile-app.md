> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 给手机安装并使用设备能力

ID：`scenario-mobile-app`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

手机 / 移动端 / iOS / Android；应用 / 安装 / 拍照 / 定位 / 原生 / App / app。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 网页能否满足使用需求？
- 必需设备能力与发布渠道是什么？

## 技术职责与候选

- [React Native](../technologies/tech-react-native.md)：用 React 思路开发移动原生界面。
- [Expo](../technologies/tech-expo.md)：简化移动应用开发、构建和发布流程。
- [Flutter](../technologies/tech-flutter.md)：使用 Dart 构建多平台应用界面。

## 模块与数据流

用户流程 → 跨端UI → 原生模块 → 权限 → 构建分发。

## 实现后应观察

- 真实目标设备流程通过
- 平台权限与插件行为明确

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-mobile-app.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-mobile-app.json)。
