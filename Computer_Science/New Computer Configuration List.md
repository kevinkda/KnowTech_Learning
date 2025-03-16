# New Computer Configuration List

[toc]

## 修订记录

| 编写日期   | 作者                                    | 内容           |
| ---------- | --------------------------------------- | -------------- |
| 2025-03-15 | [Alan Huang](https://github.com/cmrhyq) | 首次创建并编写 |
|            |                                         |                |
|            |                                         |                |



## 系统相关

### 系统软件

| 软件名称              | 解释                         | 备注 |
| --------------------- | ---------------------------- | ---- |
| Clash Nyanpasu        | 梯子                         |      |
| SanDisk Security      | 移动硬盘解锁                 |      |
| Mouse without Borders | 鼠标控制多电脑               |      |
| Bandizip              | 压缩包工具                   |      |
| Gpg4Win               | Gpg密钥工具                  |      |
| Kleopatra             | Gpg密钥工具                  |      |
| 驱动精灵              | 系统驱动                     |      |
| 百度网盘              | 云网盘                       |      |
| SumatraPDF            | pdf阅读工具                  |      |
| Logitech G HUB        | 罗技鼠标驱动工具             |      |
| 网易邮箱大师          | 邮件工具                     |      |
| 影刀                  | RPA工具                      |      |
| Claude Desktop        | 对话式AI                     |      |
| 语雀                  | 在线表格                     |      |
| Steam                 | 游戏                         |      |
| Slack                 | 工作通讯                     |      |
| QQ                    | 通讯                         |      |
| 微信                  | 通讯                         |      |
| 网易云音乐            | Music                        |      |
| Google                | 浏览器                       |      |
| BCompare              | 文件对比工具                 |      |
| Typora                | Markdown编写工具             |      |
| IDEA                  | JetBrains代码编辑器          |      |
| Rider                 | JetBrains代码编辑器          |      |
| WebStorm              | JetBrains代码编辑器          |      |
| DataGrip              | JetBrains代码编辑器          |      |
| PyCharm               | JetBrains代码编辑器          |      |
| Clion                 | JetBrains代码编辑器          |      |
| Visual Studio Code    | 代码编辑器                   |      |
| Apifox                | API管理工具                  |      |
| 微信开发者工具        | 代码编辑器                   |      |
| Trae                  | AI代码编辑器                 |      |
| Git                   | 分支管理工具                 |      |
| MobaXterm             | SSH工具                      |      |
| OssBrowser            | 阿里云OSS                    |      |
| Q-Dir                 | 文件夹多开                   |      |
| Snipaste              | 截图工具                     |      |
| Obsidian              | 开源Markdown语法的流程图工具 |      |
| 腾讯桌面助手独立版    | 桌面美化工具                 |      |
| Navicat Premium 16    | 数据库连接工具               |      |

### 系统和Office激活

1. 参考Github的[MAS](https://github.com/massgravel/Microsoft-Activation-Scripts)

2. Office激活也可以使用硬盘中的Office Tool6.4.0



## 开发环境

### Git

1. 安装Git

2. 配置用户信息

   - 配置用户名和邮件地址以及代理

   - ```shell
     # 检查设置
     git config --global --list
     # 用户名、邮件地址
     git config --global user.name "John Doe"
     git config --global user.email johndoe@example.com
     # 代理
     git config http.proxy 127.0.0.1:7890
     git config https.proxy 127.0.0.1:7890
     ```

### GPG

1. 安装Gpg4Win
2. 导入密钥
   - 使用硬盘中的GPG_Comjmand.xlsx中的命令

### Java环境

1. 安装JDK
   - 使用硬盘中的JDK或者[下载](https://www.oracle.com/java/technologies/downloads/archive/)
2. [配置多版本JDK](https://blog.csdn.net/qq_33807380/article/details/135474122)
3. 配置Maven仓库的settings.xml仓库位置
   - 复制硬盘中的文件即可

### NodeJS

1. 安装的版本使用[18.20.4](https://nodejs.org/dist/)
2. 配置NodeJS的环境变量等配置
   - [参考](https://blog.csdn.net/weixin_44462773/article/details/131087728)

3. 要安装的全局包
   - vue
   - @vue/cli
   - yarn

### Python

1. 安装Python39、Python310
2. [配置环境变量](https://blog.csdn.net/qq_40584683/article/details/126954120)
3. [配置多版本python](https://blog.csdn.net/weixin_45100742/article/details/133322422)

### MySQL

1. 本地mysql要使用[免安装版](https://downloads.mysql.com/archives/community/)
2. 配置[参考](https://blog.csdn.net/qq_45344586/article/details/129286105)