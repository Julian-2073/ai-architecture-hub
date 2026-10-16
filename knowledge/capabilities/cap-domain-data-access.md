> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 数据访问与迁移

ID：`cap-domain-data-access`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

领域查询与事务 → 数据库读写。

## 关键判断

连接池、事务生命周期、迁移、SQL 计划与驱动。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [SQLAlchemy](../technologies/tech-sqlalchemy.md)
- [Prisma ORM](../technologies/tech-prisma.md)
- [Drizzle ORM](../technologies/tech-drizzle.md)

## 退出与数据

schema、迁移记录、关键 SQL、数据导出和方言差异。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-data-access.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想稳定地读写数据库，不被迁移卡住。

1. **起点**：更需要ORM效率还是复杂SQL控制？
2. **简单或既有路线**：复用既有驱动与迁移方式；关键SQL和事务可观察。
3. **升级条件**：模型和查询复杂度证明需要时比较ORM或其他访问层。
4. **验证重点**：连接池、事务回滚、索引、迁移和锁文件。

[对应模板](../templates/template-migration.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-data-access.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-data-access.json)。
