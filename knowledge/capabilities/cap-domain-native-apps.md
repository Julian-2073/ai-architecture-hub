> 社区版：本文为作者编制的候选知识与选型建议。第三方网页正文及私人项目证据未随包分发；外部事实、版本、许可与维护状态在使用前复核，本文不证明工具已安装或项目已运行。

# 移动与桌面应用

ID：`cap-domain-native-apps`。能力分类建议，不是采用决定或项目实测。

## 职责与接口

应用状态与系统事件 → 可安装应用和原生动作。

## 关键判断

真机、原生插件、系统权限、签名、更新和分发。先复用已有实现和项目经验，仅对实际缺口调查。

## 技术入口

- [React Native](../technologies/tech-react-native.md)
- [Expo](../technologies/tech-expo.md)
- [Flutter](../technologies/tech-flutter.md)
- [Tauri](../technologies/tech-tauri.md)
- [Electron](../technologies/tech-electron.md)

## 退出与数据

业务接口、用户数据导出、平台配置及构建签名说明。

[完整能力地图](cap-software-map.md)；[社区版来源登记](../../evidence/curation/cap-domain-native-apps.json)。运行与集成均未执行，元数据见 catalog.json。

## 从业务任务作情境化判断

我想装到手机或电脑，并用本地能力。

1. **起点**：浏览器是否已满足任务？
2. **简单或既有路线**：浏览器够用时不先增加安装包；已有原生栈优先复用。
3. **升级条件**：必须设备接口、离线系统能力或分发要求时比较跨平台与原生。
4. **验证重点**：真机、系统权限、签名、插件、更新和回退。

[对应模板](../templates/template-compatibility.md)；判断属于 [社区版来源登记](../../evidence/curation/cap-domain-native-apps.json)，不是运行通过证据。

## 公开版验证状态

材料、版本与许可、PoC、项目集成及运行验收均未在本公开版执行。外部参考链接与编制边界见[来源登记](../../evidence/curation/cap-domain-native-apps.json)。
