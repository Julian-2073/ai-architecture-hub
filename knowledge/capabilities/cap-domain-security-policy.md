> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 权限策略与供应链检查

## 从业务描述开始

需要身份认证、对象授权、统一策略，还是依赖与凭证检查？

## 能力接口

可信身份/资源/规则或依赖 → 授权决定或风险发现。这是职责示意，不是固定API。

## 情境化决策分支

1. 少量稳定角色：优先框架原生或简单RBAC。
2. 共享和继承关系突出：比较关系型授权；明确撤权与列表过滤。
3. 跨服务策略一致性：评估策略引擎及执行点，防止只有策略没有拦截。
4. 供应链与秘密风险：分别扫描依赖、镜像、配置和凭证；结果须结合真实影响处理。

## 候选与关系

- [Casbin](../technologies/tech-casbin.md)：按模型与策略判断访问是否允许。
- [OpenFGA](../technologies/tech-openfga.md)：根据用户对象关系执行细粒度授权查询。
- [Open Policy Agent](../technologies/tech-opa.md)：将策略决定从应用或基础设施执行中分离。
- [Trivy](../technologies/tech-trivy.md)：扫描依赖、镜像与相关配置风险。
- [OSV-Scanner](../technologies/tech-osv-scanner.md)：依据依赖和漏洞数据发现已知风险。
- [Gitleaks](../technologies/tech-gitleaks.md)：检测仓库或文件中可能泄露的凭证。

## 关键验证与退出

核查：默认拒绝、跨租户、对象/字段/文件、策略发布、误报和升级。

保留：策略模型、资源ID、决策测试、扫描配置与处理依据。

[情境决策树模板](../templates/template-selection-decision-tree.md)、[完整地图](cap-software-map.md)。建议来自 [社区版来源登记](../../evidence/curation/cap-domain-security-policy.json)，没有执行候选软件或项目验收。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-security-policy.json)。
