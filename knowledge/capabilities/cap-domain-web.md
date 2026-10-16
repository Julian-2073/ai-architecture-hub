> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# Web 应用与构建

ID：`cap-domain-web`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

业务状态与路由 → 页面与构建产物。

## 关键判断

运行时版本、SSR/浏览器边界、路由、构建和目标托管。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [React](../technologies/tech-react.md)
- [Vue](../technologies/tech-vue.md)
- [Svelte](../technologies/tech-svelte.md)
- [Angular](../technologies/tech-angular.md)
- [Next.js](../technologies/tech-nextjs.md)
- [Nuxt](../technologies/tech-nuxt.md)
- [Astro](../technologies/tech-astro.md)
- [Vite](../technologies/tech-vite.md)
- [TypeScript](../technologies/tech-typescript.md)

## 退出与数据

源码、路由约定、数据接口、构建与部署配置。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-web.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想做一个网站或交互应用。

1. **起点**：内容为主还是大量用户状态和操作？
2. **简单或既有路线**：已有框架与路由优先复用；简单内容可用静态路线。
3. **升级条件**：确需服务端渲染、复杂路由或服务端能力时比较应用框架。
4. **验证重点**：目标设备、首屏、路由、缓存和部署入口。

[对应模板](../templates/template-selection-decision-tree.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-web.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-web.json)。
