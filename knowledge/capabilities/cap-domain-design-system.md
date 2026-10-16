> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# UI 与设计系统

ID：`cap-domain-design-system`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

组件属性与交互事件 → 一致界面。

## 关键判断

主题、焦点、键盘、包体、设计规范和商业组件边界。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [Tailwind CSS](../technologies/tech-tailwind.md)
- [Ant Design](../technologies/tech-antd.md)
- [shadcn/ui](../technologies/tech-shadcn.md)
- [Radix Primitives](../technologies/tech-radix.md)
- [Mantine](../technologies/tech-mantine.md)
- [MUI](../technologies/tech-mui.md)

## 退出与数据

业务组件、主题 token、交互规范与无障碍检查。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-design-system.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想快速做一致、好用的界面。

1. **起点**：标准后台还是高度定制的品牌界面？
2. **简单或既有路线**：先用现有设计系统与组件；标准组件覆盖就直接组合。
3. **升级条件**：需要深度控制时比较基础组件与源码控制，接受相应维护责任。
4. **验证重点**：键盘焦点、主题、输入法与真实流程，不只看默认截图。

[对应模板](../templates/template-acceptance.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-design-system.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-design-system.json)。
