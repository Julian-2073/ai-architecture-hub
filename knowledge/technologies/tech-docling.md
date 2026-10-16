> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# Docling

> 文档解析与结构化工具。候选；需按项目情境核查，不等于已采用。

## 用户想完成什么

将文档内容与结构转换为可处理表示。定位来自官方资料；下面的情境判断、组合和验证是作者建议。

## 什么时候考虑

RAG、搜索与文档管线需要结构化输入。先检查当前项目和平台已有能力；同一技术在不同业务条件下可以有不同采用决定。

## 选择分界与组合

解析质量、模型资源、表格和OCR效果由具体文件决定。

原生提取、OCR、版面和业务字段分层；Tesseract/PaddleOCR与Docling/Unstructured有重叠也有组合关系，按具体任务验证。

## 接入前提

- 核实具体产品/发行版/版本、依赖与锁文件；HEAD和网页示例不是应直接采用的稳定配置。
- 重点检查：样本分层、人工真值、漏页、字符和字段、来源定位与删除传播。
- 明确数据来源、对象权限、错误与恢复、维护人及可导出格式；官方能力不自动补齐业务规则。

## 会改变选择的验证

标注样本验证阅读顺序、表格、图片和来源定位。事先确定代表性数据、目标环境、通过标准与停止条件；目前没有本项目PoC、集成或运行通过证据。

## 成本、维护与退出

模型、算力与格式；保留原文件及可重跑解析配置。接入人力、固定运行、按量与维护分别计算；商业模块、服务、模型、字体和素材条款分别核查。未知价格和规模不估金额。

维护判断需结合支持政策、变更和安全信息；本次只记录正文中明确的具体提示，不凭热度决定成熟度。

## 证据与状态

- [官方入口](https://docling-project.github.io/docling/)；[项目或仓库入口](https://github.com/docling-project/docling)。
- [社区版来源登记](../../evidence/curation/tech-docling.json)：`src-community-tech-docling`，inference；读取日期2026-10-16，不当作网页发布日期。
- [社区版来源登记](../../evidence/curation/tech-docling.json)：`src-community-tech-docling`，inference。
- 目标版本、许可、PoC、集成和运行状态以 catalog.json 的 validations 为准，未因收录升级。

[所属能力域](../capabilities/cap-domain-document-extraction.md) · [情境决策树模板](../templates/template-selection-decision-tree.md) · [技术目录](../../docs/technology-catalog.md)

## 接入合同/票据复核流程

将结构化文档表示连接到字段候选时，另定义字段含义、来源回读、缺失与冲突状态、人工修订。解析器输出不替代业务确认或保存事务；按原件类型选择最少必要解析路线。

[管线与接口分界](../capabilities/cap-domain-document-extraction.md)、[社区版来源登记](../../evidence/curation/tech-docling.json)。本节为inference，未新增候选软件执行证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/tech-docling.json)。
