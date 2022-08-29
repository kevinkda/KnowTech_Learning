# 学习记录文档

[toc]

## 一、代码

### 1、前端

#### nodeJS 的 npm 设置国内高速镜像之淘宝镜像的方法

1、我们知道 nodeJS 是老外搞出来的，服务器放在了国外，国内的小朋友访问起来会比较慢，阿里巴巴的淘宝给出了有力支持，现在我们就将 nodeJS 的镜像地址切换为国内的淘宝镜像。

2、查看当前的镜像地址：
　　`npm get registry`
　　得到
　　`https://registry.npmjs.org/`

3、在 CMD 中执行如下命令，配置注册的镜像地址为淘宝镜像：
　　`npm config set registry http://registry.npm.taobao.org/`
　　或
　　`yarn config set registry http://registry.npm.taobao.org/`

4、如果想换回来的话将淘宝镜像再换成 `https://registry.npmjs.org/` 即可：
　　`npm config set registry https://registry.npmjs.org/`

5、备注：
　　NPM = NodeJS Package Manager

#### Vue

##### 项目构建

```bash
# 全局安装 vue-cli
$ cnpm install --global vue-cli
# 创建一个基于 webpack 模板的新项目
$ vue init webpack my-project
# 这里需要进行一些配置，默认回车即可
This will install Vue 2.x version of the template.

For Vue 1.x use: vue init webpack#1.0 my-project

? Project name my-project
? Project description A Vue.js project
? Author runoob <test@runoob.com>
? Vue build standalone
? Use ESLint to lint your code? Yes
? Pick an ESLint preset Standard
? Setup unit tests with Karma + Mocha? Yes
? Setup e2e tests with Nightwatch? Yes

   vue-cli · Generated "my-project".

   To get started:
   
     cd my-project
     npm install
     npm run dev
   
   Documentation can be found at https://vuejs-templates.github.io/webpack
```

```base
$ cd my-project
$ cnpm install
$ cnpm run dev
 DONE  Compiled successfully in 4388ms

> Listening at http://localhost:8080
```



##### 一些常用的依赖

- `npm config set registry https:*//registry**.npm**.taobao**.org*`  更换源至淘宝
- `npm install-g cnpm --registry=https://registry.npm.taobao.org ` 设置淘宝镜像
- `cnpm install express` express
- `cnpm install webpack -g` 安装webpack
- `cnpm install vue-cli -g` vue脚手架
- `cnpm install axios -S` axios
- `cnpm install element-ui -S` elementUI
- `cnpm install less less-loader --save-dev`
- `npm install vuex --save`
- `cnpm install babel-polyfill`  -- 解决白屏问题 
- `cnpm install ex6-promise`
- `npm install css-loader style-loader –save-dev`



##### 项目打包

`npm run build`
执行完后会在项目中下生成`dist`目录，一般包含 index.html 文件及 static 目录，static 目录包含了静态文件 js、css 以及图片目录 images。



##### 项目结构

| build        | 项目构建(webpack)相关代码                                    |
| ------------ | ------------------------------------------------------------ |
| config       | 配置目录，包括端口号等。我们初学可以使用默认的。             |
| node_modules | npm 加载的项目依赖模块                                       |
| src          | 这里是我们要开发的目录，基本上要做的事情都在这个目录里。里面包含了几个目录及文件：assets: 放置一些图片，如logo等。components: 目录里面放了一个组件文件，可以不用。App.vue: 项目入口文件，我们也可以直接将组件写这里，而不使用 components 目录。main.js: 项目的核心文件。 |
| static       | 静态资源目录，如图片、字体等。                               |
| test         | 初始测试目录，可删除                                         |
| .xxxx文件    | 这些是一些配置文件，包括语法配置，git配置等。                |
| index.html   | 首页入口文件，你可以添加一些 meta 信息或统计代码啥的。       |
| package.json | 项目配置文件。                                               |
| README.md    | 项目的说明文档，markdown 格式                                |



### 2、后端

#### Spring boot 和 Spring Cloud 各个版本对应关系

| spring cloud        | spring boot                                   |
| ------------------- | --------------------------------------------- |
| Finchley            | 2.0.x                                         |
| Finchley.SR1        | Spring Boot >=2.0.3RELEASE and <=2.0.9RELEASE |
| Finchley.SR4        | Spring Boot >=2.0.3RELEASE and <=2.0.9RELEASE |
| Greenwich           | 2.1.x                                         |
| Hoxton              | 2.2.x , 2.3.x(Starting with SR5)              |
| 2020.0.x aka Ilford | 2.4.x                                         |



## 二、工具：

### 1、Postman客户端中文设置

+ 下载对应版本的 [app.zip](https://gitee.com/hlmd/PostmanCn/releases)
+ 进入 Postman安装目录/版本/resources 目录
+ 将app.zip 复制解压到resources中
+ 重启Postman

### 2、windows环境的Redis启动

- 命令行窗口输入`redis-server.exe redis.windows.conf`

- `Redis-cli.exe`用于连接客户端



## 三、数据库

### 1、CentOS7 MySql数据库安装配置

#### 系统环境

yum update升级以后的系统版本

`cat /etc/redhat-release`

#### MySql安装

`yum install mysql`

`yum install mysql-server`

`yum install mysql-devel`

#### 在安装mysql-server中若出现安装失败则使用一下两种方法

##### 一.安装mariadb

`yum install mariadb-server mariadb`

mariadb数据库的相关命令：

- systemctl start mariadb  #启动MariaDB

- systemctl stop mariadb  #停止MariaDB

- systemctl restart mariadb  #重启MariaDB

- systemctl enable mariadb  #设置开机启动

##### 启动数据库

`systemctl start mariadb`

`mysql -u root -p` 没有密码

##### 二.官网下载安装mysql-server

`wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm`

`rpm -ivh mysql-community-release-el7-5.noarch.rpm`

`yum install mysql-community-server`

安装成功后重启mysql

`service mysqld restart`

进入mysql

`mysql -u root `没有密码



### 2、连接虚拟机中的MySql数据库

- 首先在linux中测试本地连接，表示mysql是可以连接的
- `netstat -apn|grep 3306`,如果显示的是127.0.0.1:3306 则修改 /etc/mysql/mysql.conf.d/mysqld.cnf 中的bind-adress 为127.0.0.1
- 然后`service mysql restart` 再次 `netstat -apn|grep 3306` 如果显示的是: : 3306则成功
- 然后修改远程登陆权限
  - 本地登录mysql
  - 方法一：
    - `use mysql;`
    - `update user set host='%' where user='root';`
  - 方法二：
    - `grant all privileges on *.* to 'root'@'%' identififed by '密码' with grant option;`
- 然后 `flush privileges;` 刷新权限



### 3、Linux中MySql常用命令：

#### 一、启动相关

1.linux下启动mysql的命令：

- mysqladmin start
  /ect/init.d/mysql start (前面为mysql的安装路径)

2.linux下重启mysql的命令：

- mysqladmin restart
  /ect/init.d/mysql restart (前面为mysql的安装路径)

3.linux下关闭mysql的命令：

- mysqladmin shutdown
  /ect/init.d/mysql shutdown (前面为mysql的安装路径)

4.连接本机上的mysql：

- 进入目录mysql\bin，再键入命令mysql -uroot -p， 回车后提示输入密码。
  退出mysql命令：exit（回车）

5.修改mysql密码：

- mysqladmin -u用户名 -p旧密码 password 新密码
  或进入mysql命令行SET PASSWORD FOR root=PASSWORD("root");

6.增加新用户。（注意：mysql环境中的命令后面都带一个分号作为命令结束符）

- grant select on 数据库.* to 用户名@登录主机 identified by "密码"
  如增加一个用户test密码为123，让他可以在任何主机上登录， 并对所有数据库有查询、插入、修改、删除的权限。首先用以root用户连入mysql，然后键入以下命令：
  grant select,insert,update,delete on *.* to " Identified by "123";

#### 二、有关mysql数据库方面的操作

必须首先登录到mysql中，有关操作都是在mysql的提示符下进行，而且每个命令以分号结束

1、显示数据库列表。

- `show databases;`

2、显示库中的数据表：

- `use mysql`； // 打开库
- `show tables;`

3、显示数据表的结构：

- `describe 表名;`

4、建库：

- `create database 库名;`
- **GBK:** `create database test2 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;`
- **UTF8:** CREATE DATABASE `test2` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

5、建表：

- `use 库名；`
- `create table 表名(字段设定列表);`

6、删库和删表:

- `drop database 库名;``
- ``drop table 表名；`

7、将表中记录清空：

- `delete from 表名;`
- `truncate table 表名;`

8、显示表中的记录：

- `select * from 表名;`

9、编码的修改
如果要改变整个mysql的编码格式： 
启动mysql的时候，`mysqld_safe`命令行加入 

- `--default-character-set=gbk `

如果要改变某个库的编码格式：在mysql提示符后输入命令 
-  `alter database db_name default character set gbk;`

10.重命名表

- `alter table t1 rename t2;`

11.查看sql语句的效率

- `explain < table_name >`
  例如：`explain select * from t3 where id=3952602;`

12.用文本方式将数据装入数据库表中(例如D:/mysql.txt)
`LOAD DATA LOCAL INFILE "D:/mysql.txt" INTO TABLE MYTABLE;`

#### 三、数据的导入导出

1、文本数据转到数据库中
文本数据应符合的格式：字段数据之间用`tab键`隔开，`null值`用来代替。例：

1 name duty 2006-11-23
数据传入命令 `load data local infile "文件名" into table 表名;`

2、导出数据库和表

- `mysqldump --opt news > news.sql`
  - 将数据库news中的所有表备份到news.sql文件，news.sql是一个文本文件，文件名任取。
- `mysqldump --opt news author article > author.article.sql`
  - 将数据库news中的author表和article表备份到author.article.sql文件， author.article.sql是一个文本文件，文件名任取。
- `mysqldump --databases db1 db2 > news.sql`
  - 将数据库dbl和db2备份到news.sql文件，news.sql是一个文本文件，文件名任取。
- `mysqldump -h host -u user -p pass --databases dbname > file.dump`
  - 就是把host上的以名字user，口令pass的数据库dbname导入到文件file.dump中
- `mysqldump --all-databases > all-databases.sql`
  - 将所有数据库备份到all-databases.sql文件，all-databases.sql是一个文本文件，文件名任取。

3、导入数据

- `mysql < all-databases.sql`
  - 导入数据库

- `mysql>source news.sql;`
  - 在mysql命令下执行，可导入表
  - 

### 4、新创建的MySql需要做的

#### 一、连接MySQL 

格式：`mysql -h主机地址 -u用户名 －p用户密码`

1、例1：连接到本机上的MYSQL。

首先在打开DOS窗口，然后进入目录 `mysqlbin`，再键入命令`mysql -uroot -p`，回车后提示你输密码，如果刚安装好`MYSQL`，超级用户`root`是没有密码的，故直接回车即可进入到`MYSQL`中了，`MYSQL`的提示符是： `mysql>`

2、例2：连接到远程主机上的`MYSQL`。假设远程主机的IP为：`110.110.110.110`，用户名为root,密码为`abcd123`。则键入以下命令：

`mysql -h110.110.110.110 -uroot -pabcd123`

（注:u与root可以不用加空格，其它也一样）

3、退出MYSQL命令： `exit` （回车）。

#### 二、修改密码

格式：`mysqladmin -u用户名 -p旧密码 password 新密码`

1、例1：给`root`加个密码`ab12`。首先在DOS下进入目录`mysqlbin`，然后键入以下命令：

`mysqladmin -uroot -password ab12`

注：因为开始时`root`没有密码，所以-p旧密码一项就可以省略了。

2、例2：再将`root`的密码改为`djg345`。

`mysqladmin -uroot -pab12 password djg345`

3、例3：通过sql语句修改

```java
-- 格式：mysql> 
set password for 用户名@localhost = password(‘新密码’);
-- 例子：mysql> 
set password for root@localhost = password(‘abc123456’);
```

#### 三、增加新用户。（注意：和上面不同，下面的因为是MySQL环境中的命令，所以后面都带一个分号作为命令结束符）

格式：`grant select on 数据库.* to 用户名@登录主机 identified by "密码"`

**例1**、增加一个用户`test1`密码为`abc`，让他可以在任何主机上登录，并对所有数据库有查询、插入、修改、删除的权限。首先用以`root`用户连入`MySQL`，然后键入以下命令：

```mysql
grant select,insert,update,
delete on *.* to test1@"%" Identified by "abc";
```

但例1增加的用户是十分危险的，你想如某个人知道test1的密码，那么他就可以在internet上的任何一台电脑上登录你的MySQL数据库并对你的数据可以为所欲为了，解决办法见例2。

**例2**、增加一个用户`test2`密码为`abc`,让他只可以在`localhost`上登录，并可以对数据库`mydb`进行查询、插入、修改、删除的操作 (`localhost`指本地主机，即`MySQL`数据库所在的那台主机)，这样用户即使用知道`test2`的密码，他也无法从`internet`上直接访问数据 库，只能通过`MySQL`主机上的web页来访问。

```mysql
grant select,insert,update,
delete on mydb.* to test2@localhost identified by "abc";
```

如果你不想`test2`有密码，可以再打一个命令将密码消掉。

```mysql
grant select,insert,update,delete on mydb.* to test2@localhost identified by "";
```

启动：`net start mySql;`
进入：`mysql -u root -p/mysql -h localhost -u root -p databaseName;`
列出数据库：`show databases;`
选择数据库：`use databaseName;`
列出表格：`show tables；`
显示表格列的属性：`show columns from tableName；`
建立数据库：`source fileName.txt;`
匹配字符：可以用通配符_代表任何一个字符，％代表任何字符串;
增加一个字段：`alter table tabelName add column fieldName dateType;`
增加多个字段：`alter table tabelName add column fieldName1 dateType,add columns fieldName2 dateType;`
多行命令输入: 注意不能将单词断开;当插入或更改数据时，不能将字段的字符串展开到多行里，否则硬回车将被储存到数据中;
增加一个管理员帐户：`grant all on *.* to user@localhost identified by "password";`
每条语句输入完毕后要在末尾填加分号';'，或者填加'\g'也可以；
查询时间：`select now();`
查询当前用户：`select user();`
查询数据库版本：`elect version();`
查询当前使用的数据库：`select database();`

1、删除student_course数据库中的students数据表：
rm -f student_course/students.*

2、备份数据库：(将数据库test备份)
mysqldump -u root -p test>c:\test.txt
备份表格：(备份test数据库下的mytable表格)
mysqldump -u root -p test mytable>c:\test.txt
将备份数据导入到数据库：(导回test数据库)
mysql -u root -p test

3、创建临时表：(建立临时表zengchao)
create temporary table zengchao(name varchar(10));

4、创建表是先判断表是否存在
create table if not exists students(……);

5、从已经有的表中复制表的结构
create table table2 select * from table1 where 1<>1;

6、复制表
create table table2 select * from table1;

7、对表重新命名
alter table table1 rename as table2;

8、修改列的类型
alter table table1 modify id int unsigned;//修改列id的类型为int unsigned
alter table table1 change id sid int unsigned;//修改列id的名字为sid，而且把属性修改为int unsigned

9、创建索引
alter table table1 add index ind_id (id);
create index ind_id on table1 (id);
create unique index ind_id on table1 (id);//建立唯一性索引

10、删除索引
drop index idx_id on table1;
alter table table1 drop index ind_id;

11、联合字符或者多个列(将列id与":"和列name和"="连接)
select concat(id,':',name,'=') from students;

12、limit(选出10到20条)<第一个记录集的编号是0>
select * from students order by id limit 9,10;

13、MySQL不支持的功能
事务，视图，外键和引用完整性，存储过程和触发器


14、MySQL会使用索引的操作符号
<,<=,>=,>,=,between,in,不带%或者_开头的like

15、使用索引的缺点
1)减慢增删改数据的速度；
2）占用磁盘空间；
3）增加查询优化器的负担；
当查询优化器生成执行计划时，会考虑索引，太多的索引会给查询优化器增加工作量，导致无法选择最优的查询方案；

16、分析索引效率
方法：在一般的SQL语句前加上explain；
分析结果的含义：
1）table：表名；
2）type：连接的类型，(ALL/Range/Ref)。其中ref是最理想的；
3）possible_keys：查询可以利用的索引名；
4）key：实际使用的索引；
5）key_len：索引中被使用部分的长度（字节）；
6）ref：显示列名字或者"const"（不明白什么意思）；
7）rows：显示MySQL认为在找到正确结果之前必须扫描的行数；
8）extra：MySQL的建议；

17、使用较短的定长列
1）尽可能使用较短的数据类型；
2）尽可能使用定长数据类型；
a）用char代替varchar，固定长度的数据处理比变长的快些；
b）对于频繁修改的表，磁盘容易形成碎片，从而影响数据库的整体性能；
c）万一出现数据表崩溃，使用固定长度数据行的表更容易重新构造。使用固定长度的数据行，每个记录的开始位置都是固定记录长度的倍数，可以很容易被检测到，但是使用可变长度的数据行就不一定了；
d）对于MyISAM类型的数据表，虽然转换成固定长度的数据列可以提高性能，但是占据的空间也大；

18、使用not null和enum
尽量将列定义为not null，这样可使数据的出来更快，所需的空间更少，而且在查询时，MySQL不需要检查是否存在特例，即null值，从而优化查询；
如果一列只含有有限数目的特定值，如性别，是否有效或者入学年份等，在这种情况下应该考虑将其转换为enum列的值，MySQL处理的更快，因为所有的enum值在系统内都是以标识数值来表示的；

19、使用optimize table
对于经常修改的表，容易产生碎片，使在查询数据库时必须读取更多的磁盘块，降低查询性能。具有可变长的表都存在磁盘碎片问题，这个问题对blob数据类型更为突出，因为其尺寸变化非常大。可以通过使用optimize table来整理碎片，保证数据库性能不下降，优化那些受碎片影响的数据表。 optimize table可以用于MyISAM和BDB类型的数据表。实际上任何碎片整理方法都是用mysqldump来转存数据表，然后使用转存后的文件并重新建数据表；

20、使用procedure analyse()
可以使用procedure analyse()显示最佳类型的建议，使用很简单，在select语句后面加上procedure analyse()就可以了；例如：
select * from students procedure analyse();
select * from students procedure analyse(16,256);
第二条语句要求procedure analyse()不要建议含有多于16个值，或者含有多于256字节的enum类型，如果没有限制，输出可能会很长；

21、使用查询缓存
1）查询缓存的工作方式：
第一次执行某条select语句时，服务器记住该查询的文本内容和查询结果，存储在缓存中，下次碰到这个语句时，直接从缓存中返回结果；当更新数据表后，该数据表的任何缓存查询都变成无效的，并且会被丢弃。
2）配置缓存参数：
变量：query_cache _type，查询缓存的操作模式。有3中模式，0：不缓存；1：缓存查询，除非与 select sql_no_cache开头；2：根据需要只缓存那些以select sql_cache开头的查询； query_cache_size：设置查询缓存的最大结果集的大小，比这个值大的不会被缓存。

22、调整硬件
1）在机器上装更多的内存；
2）增加更快的硬盘以减少I/O等待时间；
寻道时间是决定性能的主要因素，逐字地移动磁头是最慢的，一旦磁头定位，从磁道读则很快；
3）在不同的物理硬盘设备上重新分配磁盘活动；
如果可能，应将最繁忙的数据库存放在不同的物理设备上，这跟使用同一物理设备的不同分区是不同的，因为它们将争用相同的物理资源（磁头）。



### 5、Oracle管理

#### 相关链接

[Oracle官方文档](https://docs.oracle.com/database/121/DBSEG/users.htm#DBSEG99778)

[Oracle新特性](https://blog.csdn.net/weixin_31758621/article/details/116294855)

[OraclePDB管理](https://blog.csdn.net/xin_shou123/article/details/123879415)

#### CDB与PDB

CDB与PDB是Oracle 12C引入的新特性，在ORACLE 12C数据库引入的多租用户环境（Multitenant Environment）中，允许一个数据库容器(CDB)承载多个可插拔数据库(PDB)。CDB全称为Container Database，中文翻译为数据库容器，PDB全称为Pluggable Database，即可插拔数据库。在ORACLE 12C之前，实例与数据库是一对一或多对一关系(RAC)：即一个实例只能与一个数据库相关联，数据库可以被多个实例所加载。而实例与数据库不可能是一对多的关系。当进入ORACLE 12C后，实例与数据库可以是一对多的关系。

![image-20220828030404818](https://image.kevinkda.cn/md/image-20220828030404818.png)

和SQL Server相对照的话，CDB与PDB是不是感觉和SQL SERVER的单实例多数据库架构是一回事呢。像PDB$SEED可以看成是master、msdb等系统数据库，PDBS可以看成用户创建的数据库。而可插拔的概念与SQL SERVER中的用户数据库的分离、附加其实就是那么一回事。

#### CDB组件

- ROOT组件
  - ROOT又叫CDB$ROOT, 存储着ORACLE提供的元数据和Common User,元数据的一个例子是ORACLE提供的PL/SQL包的源代码，Common User 是指在每个容器中都存在的用户。
- SEED组件
  - Seed又叫PDB$SEED,这个是你创建PDBS数据库的模板，你不能在Seed中添加或修改一个对象。一个CDB中有且只能有一个Seed. 这个感念，个人感觉非常类似SQL SERVER中的model数据库
- PDBS
  - CDB中可以有一个或多个PDBS，PDBS向后兼容，可以像以前在数据库中那样操作PDBS，这里指大多数常规操作。

这些组件中的每一个都可以被称为一个容器。因此，ROOT(根)是一个容器，Seed(种子)是一个容器，每个PDB是一个容器。每个容器在CDB中都有一个独一无二的的ID和名称。

#### Oracle角色说明

- connect（连接角色）
  - 这种角色下只可以登录Oracle，不可用创建实体，也不可用创建数据库结构，即只能对其他人创建的表中的数据进行操作。

- resource(资源角色)
  - 该角色可以创建实体，但是不可以创建数据库结构。 可以创建表、序列（sequence）、运算符(operator)、过程(procedure)、触发器(trigger)、索引(index)、类型(type)和簇(cluster)。

- dba（数据库管理员权限）
  - 该角色拥有系统最高权限，只有DBA才可以创建数据库结构。包括无限制的空间限额和给其他用户授予各种权限的能力，system由dba用户拥有。
    对于普通用户来说，授予connect和resource权限即可，只对dba授予connect、resource和dba权限。

#### SqlPlus命令

##### 系统相关

- 查询oracle版本

```sql
select *
from V$VERSION;
重启数据库
​```sql
shutdown immediate;
startup;
```
- 当前连接数

```sql
select count(*) from v$process;
```
- 数据库允许的最大连接数

```
select value from v$parameter where name = 'processes'
```
- 修改最大连接数:

```sql
alter system set processes = 2000 scope = spfile;
```

- 数据库服务器配置`tnsnames`,方便后期运维操作
```shell
# 添加前最好先备份下,vim tnsnames.ora编辑文件，仔细检查，不要配置错误
cd $ORACLE_HOME/network/admin/
```
  - 格式如下
```ora
TESTRAC =
	(DESCRIPTION =
		(ADDRESS = (PROTOCOL = TCP)(HOST = scan域名)(PORT = 1521))
	(CONNECT_DATA =
	(SERVER = DEDICATED)
	(SERVICE_NAME = TESTRAC )
)
```



##### PDB相关

- 查看CDB信息

```sql
select name, cdb, open_mode, con_id
from v$database;
```
- 查看PDB实例

```sql
select name, con_id, open_mode
from V$PDBS;
```
- 查看已有pdb的tempfile文件

```sql
select name
from V$TEMPFILE;
```
- 查看已有的PDB的datafile

```sql
select name
from V$DATAFILE;
```
- 创建一个新的PDB

- 密码大小写是否敏感可以在CDB下查看该参数: show parameter sensitive

- `file_name_convert`参数参数格式：`/opt/oracle/oradata/${SID}/pdbseed, /opt/oracle/oradata/${SID}/${PDB_Name}`

```sql
create pluggable database dev admin user dev identified by 123 file_name_convert =('/opt/oracle/oradata/ORCLCDB/pdbseed','/opt/oracle/oradata/orcl_root_dev');
```
- 启动或关闭一个创建好的PDB

```sql
alter pluggable database dev open;
alter pluggable database pdb1 close;
```
- 切换到指定PDB

```sql
alter session set container=pdb1;
```
- 查看配置文件default

```sql
-- FAILED_LOGIN_ATTEMPTS --用户失败登录尝试次数
-- PASSWORD_LIFE_TIME--用户密码生命周期（按规定要求是配置3个月90天）
-- PASSWORD_VERIFY_FUNCTION--密码校验函数
-- PASSWORD_GRACE_TIME--密码失效宽容期限(30天的宽容期限)
select * from dba_profiles;
```

- 删除PDB

```sql
-- 关闭所有节点下的指定PDB，PDB处于关闭状态才能删除
show pdbs；
-- 首先在所有节点上停止实例（PDB）
alter pluggable database testrac close immediate;
-- 单节点执行删除命令
drop pluggable database testrac including datafiles;
```

- 创建一个模式

Oracle是不支持创建自定义模式的，想要创建模式的话只能新建一个用户，每个用户会有一个默认的和用户名相同的模式

```sql
CREATE SCHEMA "svc_bitbucket" AUTHORIZATION SYSTEM;
```

- 创建角色

创建的角色可以由表或系统权限或者两者的组合构成

```sql
-- 创建角色
create role myRole;
-- 授权角色
-- 如使myRole获得了在mytable中使用select进行查询的权限
grant select on mytable to myRole;
-- 再比如为角色赋予创建会话的权限
grant create session to myRole;
-- 删除角色
drop role myRole;
```



##### 用户相关

- 创建用户，对于普通用户名，用户创建的普通用户名必须以C##（或c##）开头。

```sql
create user c##svc_res identified by 123;
```
- 更改用户

```sql
alter user pdb identified by 321
```

- 授权

```sql
-- 授权
grant connect, resource to c##svc_res;
-- 撤销授权
revoke connect, resource from C##SVC_res;
```
- 查看当前用户

```sql
show user;
```
- 删除用户

```sql
-- cascade操作需要谨慎，cascade代表代表着联级删除用户名下所有的表和视图
drop user c##svc_res cascade;
```
- 查看当前有哪些用户正在使用数据

```sql
SELECT osuser, a.username,cpu_time/executions/1000000||'s', sql_fulltext,machine
from v$session a, v$sqlarea b
where a.sql_address =b.address order by cpu_time/executions desc;
```
- 用户授权，开启密码校验

```sql
-- 切换到对应的PDB下
alter session set container=PDB1;
show pdbs;
-- 授予dba、resource、connect角色权限
grant dba,resource,connect to pdb1;
-- 查看用户角色
select * from dba_role_privs where grantee = 'PDB1' and granted_role in ('DBA','RESOURCE','CONNECT')
-- 开启PDB下的用户密码校验
@?/rdbms/admin/utlpwdmg.sql
```

- 设置用户失效
  - 旨在要求使用方强制修改密码，提高密码安全性和复杂度，避免由我方运维人员知晓

```sql
alter user testrac password expire;
select username,account_status from dba_users where oracle_maintained='N';
```



## 四、Linux方面

[VMwear安装Centos7](https://www.jianshu.com/p/ce08cdbc4ddb?utm_source=tuicool&utm_medium=referral)

### 1、Linux或Git查看二进制文件

1、vim -b (需要修改的二进制文件名称)

2、`:%!xxd`

3、输入vim的修改指令，然后修改编辑二进制文件

4、编辑完后按ESC键回到指令模式

5、`:%!xxd -r`

6、输入vim的保存指令



### 2、Linux根据日期删除文件

#### find命令参数说明

```shell
# 最后一次访问发生在 n分钟 之内
-amin -n
# 最后一次访问发生在距离当前时间 n分钟 至 (n+1)分钟
-amin n
# 最后一次访问发生在 (n+1)分钟 之外
-amin +n
# 最后一次访问发生在 n天 之内
-atime -n
# 最后一次访问发生在 n天 至 (n+1)天
-atime n
# 最后一次访问发生在 (n+1)天 之外
-atime +n
# 最后一次文件状态修改发生在 n分钟 之内
-cmin -n
# 最后一次文件状态修改发生在 n分钟 至 (n+1)分钟
-cmin n
# 最后一次文件状态修改发生在 (n+1)分钟 之外
-cmin +n
# 最后一次文件状态修改发生在 n天 之内
-ctime -n
# 最后一次文件状态修改发生在 n天 至 (n+1) 天
-ctime n
# 最后一次文件状态修改发生在 (n+1)天 之外
-ctime +n
# 最后一次文件内容修改发生在 n分钟 之内
-mmin -n
# 最后一次文件内容修改发生在 n分钟 至 (n+1)分钟
-mmin n
# 最后一次文件内容修改发生在 (n+1)分钟 之外
-mmin +n
# 最后一次文件内容修改发生在 n天 之内
-mtime -n
# 最后一次文件内容修改发生在 n天 至 (n+1)天
-mtime n
# 最后一次文件内容修改发生在 (n+1)天 之外
-mtime +n
```

**例子**

```shell
# 找到两天以外的文件
find /home/xxx/pyscripts/AutoCreate/rg_task/files/ -name "*" -mtime +2 
```

```shell
# 找到两天以外的文件并删除 利用 -exec参数，如果查找有返回，可在exec参数后加上需要操作的命令，查找结果用{}来代替
find /home/xxx/pyscripts/AutoCreate/rg_task/files/ -name "*" -mtime +2 -exec rm -rfv {} \;
```




### 3、安装JDK

#### 过程

+ 查看yum库中是否有java安装包 `yum -y list java*`
+ 安装版本为1.6.X的jdk `yum -y install java-1.6.0-openjdk*`
+ 安装完成后查看版本 `java -version`



### 4、部署Tomcat

#### 过程

[Tomcat网址](https://tomcat.apache.org/download-90.cgi)

+ 下载Tomcat：

​		`wget https://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.50/bin/apache-tomcat-9.0.50.tar.gz`（注：此链接为Tomcat压缩包的地址）

+ 解压：

​		`tar -xvf apache-tomcat-9.0.50.tar.gz`

+ 进入到Tomcat下的bin目录中：

​		`cd /apache-tomcat-9.0.50.tar.gz/bin`

+ 启动：

​		`./startup.sh`

+ 验证：

​		在浏览器输入地址:127.0.0.1:8080

+ 停止服务:

​	`	./shutdown.sh`



### 5、在Idea中打包项目

#### 过程

+ 打开Project Structure界面(快捷键是F4或者F12)  选择Artifacts一栏
+ 点击＋号后选择`Web Application: Exploded`下的From Modules
+ 点击＋号后选择 `Web Application: Archive`下的For ***
+ 在右侧Name：一栏中修改名字  点击Apply和OK
+ 选择菜单栏上的Build下的Build Artifacts
+ 选择后缀之后War的那一个，之后点击Build，等待完成
+ 再打开Project Structure界面，查看Output directory一栏后的War包所在路径



### 6、Systemctl 常用命令

查看全部服务命令：

```sh
systemctl list-unit-files --type service
```

查看服务：

```sh
systemctl status name.service
```

增加开机启动：

```sh
systemctl enable name.service
```

启动服务：

```sh
systemctl start name.service
```

停止服务：

```sh
systemctl stop name.service
```

重启服务：

```sh
systemctl restart name.service
```

删除开机启动：

```sh
systemctl disable name.service
```



### 7、linux中的Tomcat 命令

- 日志类
  - `nohup ./startup.sh`  用nohup启动tomcat
  - `./catalina.sh run` tomat启动后显示控制台

#### 如何访问Tomcat页面上得manager app

- 首先进入系统中tomcat所在文件夹下的`conf`中

- 编辑`tomcat-users.xml`

- 输入以下内容，编辑好后保存退出

  ```xml
   <role rolename="manager-gui"/>
   <user username="admin" password="Hyq0901." roles="manager-gui"/>
  
    <role rolename="tomcat"/>
    <user username="tomcat" password="Hyq0901." roles="tomcat"/>
  
    <role rolename="manager-script"/>
    <user username="script" password="Hyq0901." roles="manager-script"/>
  
    <role rolename="manager-jmx"/>
    <user username="jmx" password="Hyq0901." roles="manager-jmx"/>
  
    <role rolename="manager-status"/>
    <user username="status" password="Hyq0901." roles="manager-status"/>
  
    <role rolename="admin-gui"/>
    <user username="adminGui" password="Hyq0901." roles="admin-gui"/>
  ```

- 再进入`webapps/manager/META-INF/`下编辑文件`context.xml`，将以下内容注释

  ```xml
  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
           allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
  ```

- 重启tomcat

#### 修改Tomcat项目访问路径名

- 进入tomcat所在文件夹下得conf文件夹中

- 修改`server.xml`文件，再文件底部输入以下内容

  ```XML
  <Context path="/store" docBase="store-0.0.1/" reloadble="true"/>
  ```

  - `path`代表用浏览器访问的时候的的路径，如http://localhost:8080/web来访问path=”/web”
  - `docBase`为你的项目的路径，这里同样既可以用相对路径，也可以用绝对路径。设置好了之后就会把项目自动映射到ROOT
  - `reloadable`，如果这个属性设为true，tomcat服务器在运行状态下会监视在WEB-INF/classes和WEB-INF/lib目录下class文件的改动，如果监测到有class文件被更新的，服务器会自动重新加载Web应用

- 保存退出并重启tomcat




### 8、Docker 设置elasticsearch密码

| 序号 | 账号                   | 密码     |
| ---- | ---------------------- | -------- |
| 1    | elastic                | Hyq0901. |
| 2    | apm_system             |          |
| 3    | kibana_system          |          |
| 4    | logstash_system        |          |
| 5    | beats_system           |          |
| 6    | remote_monitoring_user |          |

- 在 `elasticsearch.yml` 中添加一下代码
  - `xpack.security.enabled: true`
  - `xpack.license.self_generated.type: basic`
  - `xpack.security.transport.ssl.enabled: true`
- 在进入docker中的elasticsearch下的bin目录
  - `docker exec -it elasticsearch /bin/bash`
  - `cd bin`
- 输入以下内容
  - `elasticsearch-setup-passwords interactive`



### 9、设置命令全局的别名

#### 全局(所有用户所有终端)

```shell
# 打开系统文件
vim /etc/bashrc
# 将光标移动到文件最后一行后面，按下小o
# 粘贴或输入赋予别名的命令 
# alias [别名]='原命令'
alias grep='grep --color=auto'
# 保存文件并退出
# 重载文件
source /etc/bashrc
```

#### 局部(针对某个用户)

```shell
# 打开系统文件
vim ~/.bashrc
# 将光标移动到文件最后一行后面，按下小o
# 粘贴或输入赋予别名的命令 
# alias [别名]='原命令'
alias grep='grep --color=auto'
# 保存文件并退出
# 重载文件
source ~/.bashrc
```

#### 临时(当前终端当前用户)

```shell
# alias [别名]='原命令'
alias grep='grep --color=auto'
```



### 10、Linux设置类似$HOME的目录的快捷目录

- 第一步打开 `/etc/default/useradd` 这个文件
- 然后在最后一行写下 `名字=/目录`
- 按下ESC输入`:wq`保存并退出
- 最后输入 `source /etc/default/useradd` 或者 `source useradd`



### 11、Linux防火墙以及开放端口管理

- `systemctl status firewalld` 查看防火墙是否开启

- `systemctl start firewalld`  若没有开启则是开启状态  关闭则是 stop

- `firewall-cmd --list-ports`  查看所有开启的端口

- `firewall-cmd --zone=public --add-port=80/tcp --permanent`  防火墙开启端口访问

  --zone 作用域 --add-port=80/tcp 添加端口 端口/通讯协议 --permanent  永久生效

- `firewall-cmd --reload`  重启防火墙

- `firewall-cmd --state`  查看防火墙状态 是否是running

- `firewall-cmd --get-zones` 列出支持的zone

- `firewall-cmd --get-services` 列出支持的服务 服务是放行的

- `firewall-cmd --query-service ftp` 查看ftp服务是否支持，返回yes or no

- `firewall-cmd --remove-service=ftp --permanent` 永久移除ftp服务

- `firewall-cmd --zone=public --list-ports` 查看以开放的端口

- `netstat -Inpt` 查看监听端口

- `netstat -Inpt |grep 5672` 检查端口被那个进程占用

- `ps 6832` 查看进程的详细信息

- `kill -9 6832` 终止进程



### 12、Iptables防火墙

#### 简介：

防火墙分类

- 硬件防火墙
- 软件防火墙

#### Iptables防火墙介绍

- Linux系统内核集成了网络访问控制的功能，通过netfilter模块来实现，是内核的一部分（内核空间）
- 用户层（用户空间）可以通过iptables程序对netfilter进行控制管理，进而实现网络的访问控制
- TCP_Wrappers 也是一个网络访问控制的一个工具，作用在应用层（7层防火墙）

总结

- netfilter模块		内核空间，是内核一部分 
- iptables组件  用户空间，提供管理防火墙的手段，它主要作用在传输层（4层防火墙）

#### Iptables基本语法

- iptables [-t 表名] 命令选项 ［链名］ [规则号码] ［条件匹配］ ［-j 目标动作]

- 如果不指定表名，默认操作filter表

- 说明：
  表名和链名：用于指定 iptables命令所操作的表和链；
              命令选项：用于指定管理iptables规则的方式（比如：插入、增加、删除、查看等）；
  规则号吗：用于指定规则的编号；
  条件匹配：用于指定对符合什么样条件的数据包进行处理（比如：什么协议、出入网卡等）；
  目标动作：用于指定数据包的处理方式（比如：允许通过、拒绝、丢弃等）

- 示例

  ```shell
  iptables -L
  iptables -t filter -L
  iptables -t nat -L
  iptables -t raw -L
  iptables -t mangle -L
  ```

- 启停命令

  ```shell
  //临时停止|启动|查看状态|重新加载|重新启动
  service iptables stop|start|status|reload|restart	
  //开机是否自启动
  chkconfig iptables off|on
  //永久保存规则
  vim	/etc/sysconfig/iptables
  ```

- 常用命令

  ```shell
  常见的命令选项：
  -L								查看
  -A								追加，放置最后一条
  -I								插入，默认插入成第一条
  -D								删除
  -F								清空flush
  -P     						    设置默认策略policy
  
  处理动作：
  filter表:
  -j ACCEPT				允许
  -j DROP					丢弃，没有任何提示信息
  -j REJECT				拒绝，有提示信息
  -j LOG					写日志     /var/log/messages    然后将数据包传递给下一条规则
  nat表:
  
  -j SNAT						源地址转换 POSTROUTING
  -j DNAT						目标地址转换 PREROUTING
  ```


#### Filter表

示例：

- 全部允许/拒绝/丢弃

```shell
iptables -t filter -A INPUT -j DROP			//添加规则，丢弃所有进来的数据包
iptables -t filter -A INPUT -j ACCEPT		//添加规则，允许所有进来的数据包

//指定位置插入规则，允许所有进来的数据包第1条规则
iptables -t filter -I INPUT 1 -j ACCEPT	  

iptables -t filter -A OUTPUT -j DROP	  //添加规则，丢弃所有出去的数据包

//指定位置插入规则，拒绝所有进来的数据包为第3条规则
iptables -t filter -I INPUT 3 -j REJECT	  

iptables -t filter -L --line-numbers	  //查看规则编号
iptables -t filter -R INPUT 1 -j ACCEPT		//覆盖已有规则

iptables -t filter -D INPUT 3			//删除INPUT链的第3条规则
iptables -t filter -F					//清空filter表的所有规则

iptables -A INPUT -j LOG			//增加规则，先写日志，然后将数据包传递给下一条规则
iptables -I INPUT 2 -j DROP			

iptables -t filter -P INPUT DROP		//设置链上的默认规则
iptables -D INPUT 1
```

- 根据源和目标地址匹配

```shell
 // 匹配条件
  -s 192.168.1.1/24	源地址
  -d 192.168.1.2		目标地址
  -p tcp|upd|icmp		协议
  -i lo				input从lo接口进入得数据包
  -o eth0				output从eth0出去的数据包
  -p tcp --dport 80 	目标端口是80，需和-p tcp|upd|icmp连用
  -p udp --dport 53	目标端口是53，协议是udp
  
  //允许源地址为10.1.1.3进入
  iptables -t filter -A INPUT -s 10.1.1.3 -j ACCEPT
  //不允许源地址为10.1.1.3进入
  iptables -t filter -A INPUT ! -s 10.1.1.3 -j ACCEPT
  //拒绝源地址为10.1.1.3进入
  iptables -t filter -A INPUT -s 10.1.1.3 -j DROP
  //丢弃到达目标地址为10.1.1.3的包
  iptables -t filter -A OUTPUT -d 10.1.1.3 -j DROP
  //丢弃到达目标地址为10.1.1.3的包
  iptables -t filter -A OUTPUT ! -d 10.1.1.3 -j ACCEPT
  //丢弃所有到目标地址10.1.1.2的包	
  iptables -t filter -A INPUT -d 10.1.1.2 -j DROP
  //源地址为10.1.1.2出去的包全部允许
  iptables -t filter -A OUTPUT -s 10.1.1.2 -j ACCEPT
```

  

### 13、Vim 的使用

![image-20220828030503848](https://image.kevinkda.cn/md/image-20220828030503848.png)

#### VIM 中的替换操作

##### 语法：

- `[range]s/目标字符串/替换字符串/[option]`

##### [range]：

range 的值表示搜索范围，默认表示当前行

- range的值如果为`1,10`表示从第一行到第10行
- %表示整个文件
  - 也可以写成`1,$`
- $表示从当前行到本文件末尾

##### s：

substitute的简写，代表执行替换字符操作

##### [option]：

表示操作类型，默认只对第一个匹配的字符串进行替换

- option字段值g(global)表示全局替换
- c(comfirm)表示操作时需要确认
- i(ignorecase)表示不区分大小写

##### 例子：

- `$s/Vim/vim/gc` 会出现提示`replace with foo(y/n/a/q/l/^E/^Y)?`，询问是否确认执行
  - 待选择操作的含义包括：
  - y:确认执行这个替换将将所有Vim替换成vim;
  - n:取消这个本交Vim替换命令的操作;
  - a:执行本次所有替换字符串操作且不再询问;
  - q:退出当前vim字符串替换操作而不做任何改动;
  - l:替换完当前匹配点后退出(last)
  - Ctrl + E:向上翻滚一行
  - Ctrl + Y:向下翻滚一行



### 14、在Windows环境下安装docker

1. 首先进入[官网](https://docs.docker.com/desktop/install/windows-install/)下载安装包
2. 然后不要直接安装下载的安装包，需要根据文档提示下载并启用WSL服务
3. 进入Microsoft的[WSL安装教程网](https://docs.microsoft.com/zh-cn/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)，根据文档提示安装
4. 最后安装第一步下载的安装包



### 15、Oracle Database Docker 镜像制作

#### 相关网址

[oracle/dockerimages](https://github.com/oracle/docker-images)

##### 下载

1. 首先先前往[官网下载](https://github.com/oracle/docker-images)docker-images

##### 上传

1. 将下载的docker-images中的OracleDatabase目录上传至linux上
   1. OracleDatabase目录下的RAC应该是集群
   2. SingleInstance是单节点
   3. 根据需求进入对应目录中的dockerfiles目录下

##### 讲解

1. dockerfiles目录下包含了`11.2.0.2、``12.1.0.2、``12.2.0.1、``18.3.0、``18.4.0、``19.3.0、``21.3.0` 七个Oracle版本的文件夹
2. `buildContainerImage.sh` 用于构建镜像的脚本
3. 执行 `.buildContainerImage.sh -h` 可以看到他的帮助文档，或者前往[官网](https://github.com/oracle/docker-images/tree/main/OracleDatabase/SingleInstance)
4. 每个目录对应不通的版本，将你从官网下载的oracle版本放入到对应的目录，然后按照buildContainerImage.sh脚本的帮助文档 执行对应的命令和添加对应的参数

```
Usage: buildContainerImage.sh -v [version] -t [image_name:tag] [-e | -s | -x] [-i] [-o] [container build option]
Builds a container image for Oracle Database.

Parameters:
   -v: version to build
       Choose one of: 11.2.0.2  12.1.0.2  12.2.0.1  18.3.0  18.4.0  19.3.0  21.3.0

   -t: image_name:tag for the generated docker image
   -e: creates image based on 'Enterprise Edition'
   -s: creates image based on 'Standard Edition 2'
   -x: creates image based on 'Express Edition'
   -i: ignores the MD5 checksums
   -o: passes on container build option

* select one edition only: -e, -s, or -x

LICENSE UPL 1.0

Copyright (c) 2014,2021 Oracle and/or its affiliates.
```

##### 躲坑

![image-20220828030531150](https://image.kevinkda.cn/md/image-20220828030531150.png)

1. 第一个红圈说明了在执行 `buildContainerImage.sh` 脚本来构建每个版本的镜像时跟的参数，比如11g是-x，12c可以是-e也可以是-s

2. 第二个红圈要特别注意，需要将下载下来额Oracle包的名字改成 `linuxx64__database.zip` 这种格式，19c不需要，直接在官网下载 `Linux x86-64` 这个版本就ok，但是12c和11g不一样，如果遇到下载下来的包名字不对或者在执行脚本时报错找不到包，则需要仔细核查包名字然后修改

3. 其中 18c XE 和 21c XE 的不用下载镜像，其余版本都需要自行下载镜像

4. 11g的版本不能用 `linuxx64__database.zip` 这种格式的包，而是需要 `oracle-xe-11.2.0-1.0.x86_64.rpm.zip` 这个格式的包。

5. 每个包都需要放到对应版本的目录下

6. 以上关于 `包名字` 相关的都可以进入 `每个版本文件夹` 下，然后去查看其中的 `DockerFile` 文件

   ![image-20220828030544357](https://image.kevinkda.cn/md/image-20220828030544357.png)

##### 提醒

1. oracle11g 需要的是 oracle-xe-11.2.0-1.0.x86_64.rpm.zip 这个安装包。

2. 在镜像制作完成后 docker run的时候 要加上 --shm-size="2g" 来设置容日的内存，如果不设置可能会导致容器启动失败

3. sqlplus 出现 `ORA-12547: TNS:lost contact`

   `执行 chmod 6751 $ORACLE_HOME/bin/*`



### 16、Docker部署Oracle19c

#### 相关链接

[Oracle Database Docker 镜像制作](https://confluence.kevinkda.cn:2100/pages/viewpage.action?pageId=1900685)

[docker-compose](https://github.com/oracle/docker-images/tree/main/OracleDatabase/SingleInstance)

#### 构建工具

docker-compose

#### 构建步骤

##### 1、拉取镜像

```shell
执行命令：docker pull registry.cn-beijing.aliyuncs.com/kevinkda/env:oracle-19c-ee
```

##### 2、创建Copy镜像

```shell
docker run -d -p 1522:1522 --name oracle registry.cn-beijing.aliyuncs.com/kevinkda/env:oracle-18.4x
```

##### 3、复制Copy镜像中的文件到本地并赋权

```shell
# 复制Copy镜像中的文件到本地
docker cp oracle:/opt/oracle/oradata /mnt/remote/data/db/oracle/oracle_env_01/oradata
docker cp oracle:/opt/oracle/scripts/startup /mnt/remote/data/db/oracle/oracle_env_01/scripts/
docker cp oracle:/opt/oracle/scripts/setup /mnt/remote/data/db/oracle/oracle_env_01/scripts
# 赋权
chmod 777 oradata/ scripts/
```

##### 4、使用docker-compose启动镜像

```
version: '3.9'
services:
  oracle_env_01:
    container_name: oracle_env_01
    image: registry.cn-beijing.aliyuncs.com/kevinkda/env:oracle-19c-ee
    # restart: none
    restart: always
    privileged: true
    hostname: oracle_18x
    network_mode: bridge
    # command: sleep 36000
    # network_mode: host
    # env_file:
    #   - /mnt/remote/docker_compose/env/wiki.js.mysql.env
    environment:
      TZ: 'Asia/Shanghai'
      # ORACLE_SID: ORCLCDB
      # ORACLE_PDB: ORCLPDB1
      ORACLE_PWD: avKtYefWD@X6H3tg
    ports:
      - 1521:1521
      - 5502:5500
    volumes:
      - /etc/localtime:/etc/localtime
      # - /mnt/remote/data/db/oracle/oracle_env_01/oracle:/opt/oracle
      # - /mnt/remote/data/db/oracle/oracle_env_01/init:/docker-entrypoint-initdb.d
      - /mnt/remote/data/db/oracle/oracle_env_01/oradata:/opt/oracle/oradata
      - /mnt/remote/data/db/oracle/oracle_env_01/scripts/startup:/opt/oracle/scripts/startup
      - /mnt/remote/data/db/oracle/oracle_env_01/scripts/setup:/opt/oracle/scripts/setup
    deploy:
      resources:
        limits:
          cpus: '30.0'
          memory: 2g 
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536
        hard: 65536
```

##### 5、查看启动日志

执行命令：**docker logs -f oracle**

##### 6、oracle初始化

**连接oracle，执行命令：**docker exec -it oracle /bin/bash**
连接sysdba，执行命令：**sqlplus / as sysdba**
显示初始化的数据库，执行命令：**show pdbs**
修改 system 的密码，执行命令：**alter user system identified by system;**
修改 sys 的密码，执行命令：**alter user sys identified by sys;**
设置修改的密码永不过期，执行命令：**alter profile default limit password_life_time unlimited;**

##### 额外知识

如果需要解锁某个用户并用该用户的数据库

给某用户授予管理员权限，执行命令：**grant dba to 用户;**
更改密码，执行命令：**alter user 用户 identified by 密码;**
设置密码永不过期，执行命令：**alter profile default limit password_life_time unlimited;**
解锁用户，执行命令：**alter user 用户 account unlock**