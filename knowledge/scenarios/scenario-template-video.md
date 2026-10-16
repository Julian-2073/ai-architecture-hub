> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 把内容批量做成视频

ID：`scenario-template-video`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

批量 / 一段 / 产品介绍 / 模板 / 生成 / 自动；短视频 / 视频 / 动画 / video。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 画面模板与素材是否已有授权？
- 目标时长、比例、数量与渲染设备是什么？

## 技术职责与候选

- [Remotion](../technologies/tech-remotion.md)：用 React 组件组织视频画面和渲染。
- [FFmpeg](../technologies/tech-ffmpeg.md)：转码、封装、滤镜与流媒体处理。

## 模块与数据流

结构化内容 → 画面模板 → 渲染 → 音视频封装 → 导出。

## 实现后应观察

- 中文字体与音画同步正确
- 代表性输出可播放且内容可回读

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-template-video.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-template-video.json)。
