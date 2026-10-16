> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 本地优先、离线持久化与同步

## 从业务描述开始

仅单机离线保存，还是多设备/多人并发合并？

## 能力接口

本地变更 → 持久状态、可选复制和冲突处理。这是职责示意，不是固定API。

## 情境化决策分支

1. 单机少量键值：先看浏览器或平台原生存储。
2. 结构化查询和事务：评估索引、schema和迁移，不盲选键值封装。
3. 多人共享文档：评估CRDT，但业务约束仍由应用负责。
4. 跨设备复制：定义冲突、删除、撤权、配额与备份，不能把同步等同正确合并。

## 候选与关系

- [Dexie.js](../technologies/tech-dexie.md)：围绕 IndexedDB 组织结构化本地存储。
- [RxDB](../technologies/tech-rxdb.md)：组织响应式本地数据与复制机制。
- [localForage](../technologies/tech-localforage.md)：以异步键值接口存储本地数据。

## 关键验证与退出

核查：重启、升级、配额、离线删除、重放与数据导出。

保留：原始文档、键空间、schema、同步协议与恢复步骤。

[情境决策树模板](../templates/template-selection-decision-tree.md)、[完整地图](cap-software-map.md)。建议来自 [社区版来源登记](../../evidence/curation/cap-domain-offline-sync.json)，没有执行候选软件或项目验收。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-offline-sync.json)。
