> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# python-pptx

> Python PPTX 文档库。候选；需按项目情境核查，不等于已采用。

## 用户想完成什么

创建和修改演示文稿对象。定位来自官方资料；下面的情境判断、组合和验证是作者建议。

## 什么时候考虑

Python流水线需要PPTX处理。先检查当前项目和平台已有能力；同一技术在不同业务条件下可以有不同采用决定。

## 选择分界与组合

高级动画和Office对象覆盖有限，不能仅凭文件可打开验收。

按“数据读取 / 新建 / 修改原件 / 渲染 / OCR”分支；再按JS/Python与保真要求比较。pypdf、PDF.js与PyMuPDF职责不同；Excel文件库不自动计算公式。

## 接入前提

- 核实具体产品/发行版/版本、依赖与锁文件；HEAD和网页示例不是应直接采用的稳定配置。
- 重点检查：数据口径、公式缓存、对象保留、目标Office与渲染检查。
- 明确数据来源、对象权限、错误与恢复、维护人及可导出格式；官方能力不自动补齐业务规则。

## 会改变选择的验证

验证原模板、图表、分组与视觉渲染。事先确定代表性数据、目标环境、通过标准与停止条件；目前没有本项目PoC、集成或运行通过证据。

## 成本、维护与退出

版式与对象兼容；保留原件与编辑记录。接入人力、固定运行、按量与维护分别计算；商业模块、服务、模型、字体和素材条款分别核查。未知价格和规模不估金额。

维护判断需结合支持政策、变更和安全信息；本次只记录正文中明确的具体提示，不凭热度决定成熟度。

## 证据与状态

- [官方入口](https://python-pptx.readthedocs.io/)；[项目或仓库入口](https://github.com/scanny/python-pptx)。
- [社区版来源登记](../../evidence/curation/tech-python-pptx.json)：`src-community-tech-python-pptx`，inference；读取日期2026-10-16，不当作网页发布日期。
- [社区版来源登记](../../evidence/curation/tech-python-pptx.json)：`src-community-tech-python-pptx`，inference。
- 目标版本、许可、PoC、集成和运行状态以 catalog.json 的 validations 为准，未因收录升级。

[所属能力域](../capabilities/cap-domain-office-documents.md) · [情境决策树模板](../templates/template-selection-decision-tree.md) · [技术目录](../../docs/technology-catalog.md)

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/tech-python-pptx.json)。
