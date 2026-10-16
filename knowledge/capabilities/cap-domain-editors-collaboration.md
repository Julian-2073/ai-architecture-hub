> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 编辑器与协同画布

ID：`cap-domain-editors-collaboration`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

文档、文本或操作 → 编辑状态与持久化内容。

## 关键判断

输入法、粘贴、撤销、内容格式、冲突合并与对象权限。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [Tiptap](../technologies/tech-tiptap.md)
- [Lexical](../technologies/tech-lexical.md)
- [Monaco Editor](../technologies/tech-monaco.md)
- [CodeMirror](../technologies/tech-codemirror.md)
- [Yjs](../technologies/tech-yjs.md)
- [tldraw](../technologies/tech-tldraw.md)
- [Excalidraw](../technologies/tech-excalidraw.md)

## 退出与数据

原始文档、格式版本、协同历史与可验证导出。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-editors-collaboration.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想编辑文档、代码或让多人一起写。

1. **起点**：文档模型是什么，是否有多人和离线？
2. **简单或既有路线**：纯文本和单人编辑不必引入协作层；先看现有编辑器。
3. **升级条件**：富文本、代码语言、自由画布与共享合并按职责拆开。
4. **验证重点**：中文、粘贴、撤销、格式往返、权限和离线冲突。

[对应模板](../templates/template-sync-conflicts.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-editors-collaboration.json)，不是运行通过证据。

## 节点编辑的组合关系

[React Flow](../technologies/tech-react-flow.md)可承担节点画布、连线与选择；布局、图查询与执行语义分别判断，参见[关系图组合指南](cap-solution-relationship-workbench.md)。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-editors-collaboration.json)。
