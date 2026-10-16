> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 地理与空间数据

ID：`cap-domain-geospatial`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

坐标/区域/轨迹 → 地图或空间图层。

## 关键判断

坐标系统、底图与瓦片、数据许可、GPU 和网络。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [MapLibre GL JS](../technologies/tech-maplibre.md)
- [deck.gl](../technologies/tech-deckgl.md)

## 退出与数据

地理数据、样式、坐标说明及瓦片来源。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-geospatial.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想在地图上看门店、区域和轨迹。

1. **起点**：要显示数据还是进行空间计算？
2. **简单或既有路线**：少量标记与标准二维地图先评估简单图层。
3. **升级条件**：大量GPU图层、空间运算和三维地球分别进入专项路线。
4. **验证重点**：坐标、底图许可、地区访问和目标设备。

[对应模板](../templates/template-compatibility.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-geospatial.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-geospatial.json)。
