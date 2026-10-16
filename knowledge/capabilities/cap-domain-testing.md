> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 测试与质量保障

ID：`cap-domain-testing`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

业务场景、输入或负载 → 可复现结果与缺口。

## 关键判断

环境、目标设备、测试数据、负载授权和断言有效性。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [Playwright](../technologies/tech-playwright.md)
- [Vitest](../technologies/tech-vitest.md)
- [k6](../technologies/tech-k6.md)
- [axe-core](../technologies/tech-axe-core.md)

## 退出与数据

用例、样本、阈值、复现命令、结果与未覆盖范围。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-testing.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想自动验证功能和承载能力。

1. **起点**：最重要的失败是什么，发生在哪一层？
2. **简单或既有路线**：按风险选函数、接口或关键流程检查，复用有效证据。
3. **升级条件**：多浏览器、容量或可访问性出现实质要求时补专项验证。
4. **验证重点**：观察业务结果，不用覆盖率、截图或构建替代交付验收。

[对应模板](../templates/template-acceptance.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-testing.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-testing.json)。
