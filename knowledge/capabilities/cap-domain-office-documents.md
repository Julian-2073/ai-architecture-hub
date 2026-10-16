> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# Office、PDF 与正式文档交换

## 从业务描述开始

要提取数据、新建文件、修改原件，还是渲染阅读？

## 能力接口

原件/结构化内容 → 可编辑文件、数据或正式渲染。这是职责示意，不是固定API。

## 情境化决策分支

1. 只读数据：先核查字段、日期、空白与公式值；不要先承诺样式保真。
2. 生成新文件：按语言与目标格式选生成库；先建立内容与模板契约。
3. 修改复杂原件：对宏、修订、母版、动画、复杂图表等逐项验证，不把可打开当无损。
4. 要计算公式：独立确认计算引擎；写入公式不等于已经计算。

## 候选与关系

- [PyMuPDF](../technologies/tech-pymupdf.md)：读取、渲染和操作文档页面及内容。
- [pypdf](../technologies/tech-pypdf.md)：合并、拆分、读取和变换 PDF。
- [PDF.js](../technologies/tech-pdfjs.md)：在浏览器中解析显示 PDF。
- [docx（TypeScript）](../technologies/tech-docx-ts.md)：通过代码生成 DOCX 文档。
- [python-docx](../technologies/tech-python-docx.md)：读取和修改 DOCX 内容与结构。
- [Docxtemplater](../technologies/tech-docxtemplater.md)：将数据填入 Office 模板生成文档。
- [ExcelJS](../technologies/tech-exceljs.md)：读取生成 XLSX 并处理样式和单元格。
- [SheetJS](../technologies/tech-sheetjs.md)：解析与生成多种电子表格数据。
- [openpyxl](../technologies/tech-openpyxl.md)：操作工作簿单元格、样式与结构。
- [XlsxWriter](../technologies/tech-xlsxwriter.md)：生成含格式和图表的电子表格。
- [PptxGenJS](../technologies/tech-pptxgenjs.md)：代码化生成可编辑 PPTX。
- [python-pptx](../technologies/tech-python-pptx.md)：创建和修改演示文稿对象。

## 关键验证与退出

核查：数据口径、公式缓存、对象保留、目标Office与渲染检查。

保留：原件、模板、结构化数据、字体来源与修改范围。

[情境决策树模板](../templates/template-selection-decision-tree.md)、[完整地图](cap-software-map.md)。建议来自 [社区版来源登记](../../evidence/curation/cap-domain-office-documents.json)，没有执行候选软件或项目验收。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-office-documents.json)。
