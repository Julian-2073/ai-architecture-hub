> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 服务接口与契约

ID：`cap-domain-api`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

经验证请求 → 业务响应、事件或错误。

## 关键判断

输入、身份、对象权限、事务、超时和接口版本。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [FastAPI](../technologies/tech-fastapi.md)
- [NestJS](../technologies/tech-nestjs.md)
- [Django](../technologies/tech-django.md)
- [Pydantic](../technologies/tech-pydantic.md)
- [Zod](../technologies/tech-zod.md)
- [Express](../technologies/tech-express.md)
- [Fastify](../technologies/tech-fastify.md)
- [Hono](../technologies/tech-hono.md)
- [Spring Boot](../technologies/tech-spring-boot.md)
- [Gin](../technologies/tech-gin.md)
- [GraphQL.js](../technologies/tech-graphql.md)
- [gRPC](../technologies/tech-grpc.md)
- [tRPC](../technologies/tech-trpc.md)

## 退出与数据

接口 schema、领域逻辑、错误语义与集成契约。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-api.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想把几个系统的数据和业务接起来。

1. **起点**：是同步查询还是长任务，消费者是什么语言？
2. **简单或既有路线**：复用当前服务和标准接口；输入校验与对象权限保持明确。
3. **升级条件**：多语言强契约、复杂客户端查询或长任务语义明显时比较专项协议。
4. **验证重点**：schema、超时、错误、鉴权和业务回执。

[对应模板](../templates/template-data-contract.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-api.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-api.json)。
