---
typora-root-url: 16.Document-images\Problem-and-solution
---

# 问题和解决方案

[toc]

## 一、代码

### 1、前端

#### Vue

##### 在高版本的nodejs中创建的vue项目不能在低版本的nodejs中运行

- 重新创建项目或者升级nodejs



##### vue 项目报错 Module build failed: Error: No PostCSS Config

- 在src同级目录添加postcss.config.js文件

```js
module.exports = {
  plugins: {
    'autoprefixer': {browsers: 'last 5 version'}
  }
}
```



##### Vue项目dist文件夹不能上传至github问题

- 解决方法：
  找到vue根目录下的`.gitignore`，打开文件
- 注释掉`删除掉 /dist/ `
- 保存后重新打包上传`.gitignore`



### 2、微信小程序

#### 微信小程序上传至GitHub出现`Github warning: LF will be replaced by CRLF in`的问题

- 在项目目录下执行以下代码
  - `git config --global core.autocrlf false`



#### 微信小程序上线以后无法请求后台数据

- 问题排查发现后端已部署，通过Postman能请求数据

- 在手机打开小程序调试窗口发现报错`request:fail url not in domain list` 发现没设置合法域名

- 情况1：未设置合法域名
  解决方法:请在微信公众平台登录小程序后台设置。

- 情况2：设置了合法域名，开发工具仍然报错
  解决方法:
  在右上角点击详情，之后刷新一下项目配置，看看有无域名信息，如果有了，清除全部缓存重新编译小程序，如果还是没有请确认是否设置合法域名。

- 情况3：设置了合法域名，开发工具不报，真机调试和体验版报
  这种情况一般开发工具正常运行，真机调试和体验版不行，因为之前使用过真机调试和发布体验版，在测试机上留下缓存

  解决方法:手机微信下拉找到最近使用的小程序，长按之后拖到底部删除，然后重新尝试真机调试和体验版。

- 情况4：设置了合法域名，到哪都报错，清缓存也没用！
  解决方法:请确认访问该域名时，是否会出现重定向，将重定向域名添加进合法域名

- 情况5：设置了合法域名（含重定向），到哪都报错，清缓存也没用！
  解决方法:请确认访问该域名是否是三级域名，请设置为一级或二级域名

- 情况6：以上所有解决方案都不行！
  解决方法:请在微信小程序平台反馈bug



### 3、后端

#### 删除list中的数据发现数据还存在的问题

+ 循环删除list中特定的一个元素的，可以使用for循环遍历list、增强for循环、Iterator遍历

+ 循环删除list中多个元素时，应该使用迭代器Iterator的方式

```Java
List<String> list = new ArrayList<String>(Arrays.asList("沉", "默", "王", "二"));
Iterator<String> iter = list.iterator();
while (iter.hasNext()){
    if (iter.next().equals("默")){
        iter.remove();
    }
}
log.info("list value："+list);
```



### 4、nacos搭建问题

- 注意Spring boot 和 Spring Cloud 各个版本对应关系




## 二、工具：

### 1、PyCharm控制台报错无法加载文件 D:\PythonProject\venv\Scripts\activate.ps1

#### 概述

新安装系统后，安装完PyCharm的控制台出现问题，具体如下。

#### 问题

无法加载文件 D:\PythonProject\venv\Scripts\activate.ps1

![image-20220828030226646](https://image.kevinkda.cn/md/image-20220828030226646.png)

#### 原因

Restricted（防止运行没有数字签名的脚本），要设置成remotesigned模式

#### 解决

- 打开PowerShell
- 输入 set-ExecutionPolicy RemoteSigned

![image-20220828030208204](https://image.kevinkda.cn/md/image-20220828030208204.png)



### 2、VMware启动系统显示不支持的硬件版本

#### 问题描述：

- 虚拟机使用的是此版本VMware Workstation不支持的硬件版本。
  模块"Upgrade"启动失败。未能启动虚拟机。

![image-20220828025929110](https://image.kevinkda.cn/md/image-20220828025929110.png)

#### 解决方案:

1、找到vmware 虚拟机存放目录，使用记事本方式打开.vmx 文件。

![image-20220828030917729](https://image.kevinkda.cn/md/image-20220828030939180.png)

2、修改和自己Vmware匹配的版本号

![image-20220828030939180](https://image.kevinkda.cn/md/image-20220828030917729.png)

3、使用记事本打开.vmdk 文件

![image-20220828031024381](https://image.kevinkda.cn/md/image-20220828031024381.png)

4、修改和自己Vmware匹配的版本号

![image-20220828031039116](https://image.kevinkda.cn/md/image-20220828031039116.png)



## 三、数据库

### 1、MySql远程登陆报错：

错误信息：`Host '192.168.1.3' is not allowed to connect to this MySQL server`

- 原因：MySQL服务器要设置你的ip访问权限
- 解决方法：
  - 改表法：
    - 可能是因为使用的账号不允许远程登陆。需要在linux中登入mysql更改`mysql`数据库里的`user`表里的`host`项，从`localhost`改为`%`
      - `mysql -uroot -p`
      - `use mysql;`
      - `update user set host='%' where user='root';`
      - `flush rivileges;`
  - 授权法：
    - 例1：你想root使用123作为密码从任何主机连接到mysql服务器的；(以下操作基于登入的账户拥有完全控制权限)
      - `mysq -uroot -p`
      - `grant all privileges on *.* to 'root'@'%' identified by '123' with grant option;`
      - `flush privileges;`
    - 例2：如果你想允许用户root从ip为192.168.1.3的主机连接到mysql服务器，并使用123作为密码
      - `GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.1.3' IDENTIFIED BY '123' WITH GRANT OPTION`
      - `flush privileges;`
    - 如果你想允许用户root从ip为192.168.1.3的主机连接到mysql服务器的dk数据库，并使用123作为密码
      - `GRANT ALL PRIVILEGES ON dk.* TO 'root'@'192.168.1.3' IDENTIFIED BY '123' WITH GRANT OPTION;`
      - `flush privileges;`




### 2、Navicat连接CentOS 7 中的mysql报错10060

- 首先在自己系统的cmd中ping 一下网络是不是能ping通

- 如果用的是云服务器，则去检查安全组设置是否有问题

- 然后进入CentOS 7的Mysql中查看用户权限

  `mysql -uroot -p`

  `use mysql`;

  `select host,user from user;`

  如果root账户对应的host是%则代表是不受ip约束

- 最后一种可能性则需要去设置防火墙啦

  `firewall-cmd --permanent --zone=public --add-port=3306/tcp`

  `firewall-cmd --reload`



### 3、Navicat连接Mysql8报错2059

#### Navicat连接Mysql8报错2059-Authentication plugin 'caching_sha2_password' cannot be loaded解决方案

**原因**：

- 是mysql8.0版更换了新的身份验证是（caching_sha2_password）之前身份验证是（mysql_native_password），Navicat，和SQLyog客户端软件其实是不支持新的身份验证，也就是说新的身份验证找不到（caching_sha2_password）

**解决方案**：

- 把登录密码加密规则改回（mysql_native_password）

**操作流程**：

- 登录MySQL
  - `mysql -uroot -p****`
- 修改加密规则
  - `ALTER USER 'root'@'localhost' IDENTIFIED BY '密码' PASSWORD EXPIRE NEVER;`
- 更新用户密码
  - `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '密码';`
- 刷新权限
  - `FLUSH PRIVILEGES; `
- 重置密码
  - `alter user 'root'@'localhost' identified by '你的密码';`

**注意:**

- 若在修改加密规则或更新用户密码的时候报错`1396 (HY000): Operation ALTER USER failed for ‘root‘@‘localhost‘`
  - 将上方语句中得`localhost`改为`%`
    - 例：`ALTER USER 'root'@'%' IDENTIFIED BY '密码' PASSWORD EXPIRE NEVER;`



### 4、Oracle删除用户时必须指定 CASCADE

#### 问题描述

- 在删除用户时出现`ORA-01922: 必须指定 CASCADE 以删除 'AUTO_NCC_NEW'`

#### 原因

- 因为**这个数据库只有这一个用户**，删了就没有用户关联了，所以需要用 `cascade`，把没有关联的整个数据库也删掉。

#### 解决方法

- 在删除语句后加上一个`cascade`即可解决问题(如果数据比较多得话就会比较慢。)



### 5、Oracle删除用户时无法删除

#### 问题描述

- `ORA-01940: cannot drop a user that is currently connected`

#### 原因

- 该用户已经被连接了，所以删除不了

#### 解决方案

```sql
#找到连接的sid和端口号
select sid,serial# from v$session where username='XMH';
#杀死正在连接的session
alter system kill session '40,2121';
```



## 四、Linux方面

[VMwear安装Centos7](https://www.jianshu.com/p/ce08cdbc4ddb?utm_source=tuicool&utm_medium=referral)

### 1、CentOS 7 出现 a problem has occured and the system can‘t recover 
#### 解决办法：
+ 组合键进入命令行进行修复
#### 过程：
+ 在图形界面下，按组合键 `Ctrl+Alt+F2` 进入命令行界面
+ 依次输入以下命令进行系统修复(注意：若账户权限不足或提示没有此账户则使用 su root切换账户再执行以下命令)：
```Linux
sudo yum history package-list gjs
sudo yum history package-list gnome-shell
sudo yum update --skip-broken
```
+  注意在安装过程中全部选择“Y”，之后就是等待系统修复完成，最后输入 `sudo shutdown -r now` 重新启动系统



### 2、Linux shell脚本中CRLF和LF问题

#### 报错：-bash: ./build.sh: /usr/bin/sh^M: bad interpreter: No such file or directory

#### 问题原因

- window上换行符为CRLF ，而Linux换行符为 LF。Windos上换行是 \r\n ，Linux上换行是\r

#### 修改方法

- windows下
  - 使用nodePad++打开要修改的脚本
  - 点击视图/显示符号/显示行尾/
  - 点击replace下的search mode（搜索模式）中的Extended（扩展），进行勾选
  - 再将\r\n替换为\n
- Linux下
  - 再Linux中使用vim编辑器打开脚本
  - 进入以后按Esc键，并输入`set ff =unix