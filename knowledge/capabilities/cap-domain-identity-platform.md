> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 身份与后端平台

ID：`cap-domain-identity-platform`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

身份和访问请求 → 会话、令牌或后端能力。

## 关键判断

租户、RLS/对象权限、令牌生命周期、文件和数据导出。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [Keycloak](../technologies/tech-keycloak.md)
- [Supabase](../technologies/tech-supabase.md)

## 退出与数据

身份映射、业务用户 ID、角色、策略与数据备份。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-identity-platform.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想让不同用户安全登录，只能看允许的数据。

1. **起点**：身份与租户从何处可信地确定？
2. **简单或既有路线**：复用已有认证与简单角色；服务端落实对象权限。
3. **升级条件**：共享继承、跨服务策略或统一身份有需求再选择专项系统。
4. **验证重点**：令牌、撤权、跨租户、字段、文件与检索过滤。

[对应模板](../templates/template-authorization-matrix.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-identity-platform.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-identity-platform.json)。
