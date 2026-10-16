> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 地理几何、空间查询与三维地球

## 从业务描述开始

需要地图显示、空间计算，还是地球与地形场景？

## 能力接口

带坐标的数据 → 空间查询、地理分析或地图场景。这是职责示意，不是固定API。

## 情境化决策分支

1. 二维显示：比较轻量覆盖物与矢量图层，底图服务另核。
2. 数据库内空间查询：已有PostgreSQL时评估扩展与索引。
3. 离线地理计算：按表格/几何操作选择工具，明确投影和距离单位。
4. 三维地球：与一般产品3D展示分开；地形影像数据、坐标和GPU都需核查。

## 候选与关系

- [PostGIS](../technologies/tech-postgis.md)：空间存储、索引与几何查询。
- [GeoPandas](../technologies/tech-geopandas.md)：以表格方式处理地理对象和空间连接。
- [Shapely](../technologies/tech-shapely.md)：处理平面几何对象与空间运算。
- [Leaflet](../technologies/tech-leaflet.md)：展示瓦片地图与标记等交互。
- [CesiumJS](../technologies/tech-cesium.md)：展示地球、地形与地理空间三维数据。

## 关键验证与退出

核查：坐标参考系、单位、高度、几何有效性、数据和服务许可。

保留：标准地理格式、坐标说明、运算配置与底图来源。

[情境决策树模板](../templates/template-selection-decision-tree.md)、[完整地图](cap-software-map.md)。建议来自 [社区版来源登记](../../evidence/curation/cap-domain-geospatial-analysis.json)，没有执行候选软件或项目验收。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-geospatial-analysis.json)。
