> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 数据可视化

ID：`cap-domain-visualization`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

指标数据与筛选 → 图形及交互事件。

## 关键判断

空值、时间、单位、采样、联动和目标设备。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [Apache ECharts](../technologies/tech-echarts.md)
- [D3](../technologies/tech-d3.md)
- [AntV G2](../technologies/tech-g2.md)

## 退出与数据

原始数据、指标口径、适配函数和交互定义。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-visualization.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想把业务数字做成可筛选的图。

1. **起点**：普通统计图是否能表达任务？
2. **简单或既有路线**：标准图优先现有图表库与配置；数据口径独立定义。
3. **升级条件**：标准能力不能表达形状或交互时才承担自定义图形成本。
4. **验证重点**：指标、单位、空值、时区、联动和目标数据规模。

[对应模板](../templates/template-data-contract.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-visualization.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-visualization.json)。
