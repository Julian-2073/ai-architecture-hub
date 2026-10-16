> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 图像、视频与文档

ID：`cap-domain-media-documents`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

媒体、内容和模板 → 处理结果或正式文件。

## 关键判断

字体、透明度、方向、编码、分页、素材与发行许可。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [OpenCV](../technologies/tech-opencv.md)
- [Pillow](../technologies/tech-pillow.md)
- [FFmpeg](../technologies/tech-ffmpeg.md)
- [Remotion](../technologies/tech-remotion.md)
- [Typst](../technologies/tech-typst.md)
- [Pandoc](../technologies/tech-pandoc.md)

## 退出与数据

原始素材、模板、字体来源、参数和可编辑文件。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-media-documents.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想处理图片视频，生成可用的正式文件。

1. **起点**：是创作、格式转换、识别还是原件保留？
2. **简单或既有路线**：按具体格式与操作选小工具，保留原始素材。
3. **升级条件**：复杂排版、OCR或实时媒体另选专项链，不用一个库包打天下。
4. **验证重点**：目标应用渲染、字体、音画、对象保真和素材许可。

[对应模板](../templates/template-office-roundtrip.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-media-documents.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-media-documents.json)。
