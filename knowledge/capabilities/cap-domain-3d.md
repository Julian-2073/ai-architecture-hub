> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 三维与实时场景

ID：`cap-domain-3d`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

模型/材质/场景状态 → 资产或实时场景。

## 关键判断

模型单位、glTF 等交换格式、纹理、设备资源与素材许可。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [Three.js](../technologies/tech-threejs.md)
- [Babylon.js](../technologies/tech-babylonjs.md)
- [Blender](../technologies/tech-blender.md)
- [Godot](../technologies/tech-godot.md)

## 退出与数据

模型源文件、通用交换资产、场景和业务接口。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-3d.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想旋转看产品或交互场景。

1. **起点**：已有资产吗，需要模拟还是只是展示？
2. **简单或既有路线**：只展示时选择一种运行路线并控制资产，不默认加入仿真引擎。
3. **升级条件**：真实空间和业务规则、物理模拟需要专门模型与校准。
4. **验证重点**：模型单位、纹理、交互、设备帧率及资产授权。

[对应模板](../templates/template-poc.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-3d.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-3d.json)。
