> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 部署与基础设施

ID：`cap-domain-infrastructure`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

代码、镜像或配置 → 可运行资源与交付流程。

## 关键判断

平台架构、秘密、网络、持久卷、资源状态和授权。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [Docker](../technologies/tech-docker.md)
- [NGINX](../technologies/tech-nginx.md)
- [Caddy](../technologies/tech-caddy.md)
- [Kubernetes](../technologies/tech-kubernetes.md)
- [OpenTofu](../technologies/tech-opentofu.md)
- [Ansible](../technologies/tech-ansible.md)
- [GitHub Actions](../technologies/tech-github-actions.md)

## 退出与数据

声明配置、镜像来源、环境、状态备份和回退命令。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-infrastructure.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想把应用稳定运行起来并能更新回退。

1. **起点**：现有平台能否承担运行、存储和入口？
2. **简单或既有路线**：先用已有托管或简单服务，保持可恢复部署。
3. **升级条件**：规模、独立伸缩或团队边界确有收益时才增加集群与IaC。
4. **验证重点**：架构、网络、秘密、持久化、更新和回退。

[对应模板](../templates/template-migration.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-infrastructure.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-infrastructure.json)。
