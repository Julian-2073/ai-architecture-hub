> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 建立内容网站与产品介绍页

ID：`scenario-content-site`。这是一条任务发现与交接规则，不是已完成的软件或技术采用决定。

## 业务描述入口

文章 / 博客 / 内容 / 介绍页 / 官网 / 作品集；网站 / 页面 / 展示 / 发布 / 搜索引擎。

## 先判断什么

先检查当前项目相关实现、依赖和平台能力；现有方案够用时复用，不因匹配到场景就新增框架。

先复用当前栈；对同职责候选作比较，对跨职责组件明确接口。列表不是全部要安装的技术栈。

- 内容如何维护？
- 是否需要服务端渲染、登录或大量交互？

## 技术职责与候选

- [Astro](../technologies/tech-astro.md)：组织内容页面并按需加入交互组件。
- [Next.js](../technologies/tech-nextjs.md)：组织路由、服务端渲染与服务端逻辑。
- [Nuxt](../technologies/tech-nuxt.md)：基于 Vue 组织路由、渲染和服务端能力。

## 模块与数据流

内容 → 页面模板 → 构建或渲染 → 托管。

## 实现后应观察

- 链接和内容更新可用
- 目标设备与首屏符合要求

## 可选模板

- [简版技术选型](../templates/template-selection-brief.md)
- [架构数据流与接口边界](../templates/template-architecture-dataflow.md)

## 依据与限制

[社区版来源登记](../../evidence/curation/scenario-content-site.json)为 inference；官方组织方法参考见 [方法研究](../../docs/knowledge-design-reference.md)。工具功能和采用状态到各技术记录查看。本场景尚无项目运行验证，不能用规则命中代替选型结论。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/scenario-content-site.json)。
