> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 持久化、缓存与文件存储

ID：`cap-domain-persistence`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

记录、键值或文件 → 持久状态和查询。

## 关键判断

主副本关系、并发、备份恢复、容量、权限及许可。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [PostgreSQL](../technologies/tech-postgresql.md)
- [SQLite](../technologies/tech-sqlite.md)
- [Redis](../technologies/tech-redis.md)
- [MongoDB](../technologies/tech-mongodb.md)
- [MinIO](../technologies/tech-minio.md)

## 退出与数据

原始数据、schema、导出工具、恢复记录和访问策略。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-persistence.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想保存订单、客户和文件，能恢复数据。

1. **起点**：事实来源是事务记录、文件还是缓存？
2. **简单或既有路线**：单机低并发可评估简单方案；已有数据库优先复用。
3. **升级条件**：并发、事务、共享与恢复目标改变时再引入新存储。
4. **验证重点**：约束、备份恢复、删除、权限与事实来源一致性。

[对应模板](../templates/template-migration.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-persistence.json)，不是运行通过证据。

## 先区分四种业务责任

| 业务描述 | 先判断什么 | 技术入口与组合边界 |
|---|---|---|
| 保存订单、审批、客户修改 | 谁写入、事务、共享、持久磁盘与恢复 | 已有业务库优先；[SQLite](../technologies/tech-sqlite.md)与[PostgreSQL](../technologies/tech-postgresql.md)按部署和写入模式评估 |
| 查看历史文件、计算汇总 | 输入快照、扫描成本、查询口径、进程模型 | 可评估[DuckDB](../technologies/tech-duckdb.md)；分析结果是否回写业务库另定 |
| 重复读取很慢 | 先定位瓶颈、可接受新鲜度、失效与重建 | 必要时评估[Redis](../technologies/tech-redis.md)；缓存不能悄悄变成另一份事实 |
| 保存图片、合同原件 | 文件身份、访问权限、版本与保留 | 文件/对象存储与业务元数据分工，数据库记录文件地址不等于文件已备份 |

一个项目可以组合这些责任，但每一项都应有具体缺口才增加组件。“支持SQL”“在内存中”“文件形式”都不足以单独决定架构。

[社区版来源登记](../../evidence/curation/cap-domain-persistence.json)属于inference，不证明任何项目已采用；具体官方来源见对应卡片。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-persistence.json)。
