[TOC]

# Oracle数据库的使用

## 数据库相关概念

### 什么是数据库

所谓的数据库其实就是数据的集合。用户可以对集合中的数据进行新增、查询、更新、删除等操作。数据库是以一定方式储存在-起、能与多个用户共享、具有尽可能小的冗余度、与应用程序彼此独立的数据集合。

### 数据库类型

#### 关系型

- Oracle
- MySQL
- PostgreSQL
- DB2
- Microsoft SQL Server
- Microsoft Access

#### 非关系型

- Redis
- MongoDB
- Big Table

### 关系型数据库与非关系型数据之间的区别

#### 关系型数据库

##### 特点

- 关系型数据库最典型的数据结构是表，由二维表及其之间的联系所组成的一个数据组织。支持事务一致特性。 

##### 优点

- 易于维护：都是使用表结构，格式一致;
- 使用方便： SQL语言通用;
- 复杂操作：支持SQL，可用于一个表以及多个表之间非常复杂的查询;

##### 缺点

- 性能差：读写性能比较差，尤其是海量数据的高效率读写，传统关系型数据库来说，硬盘I/O是一个很大的瓶颈;
- 存储方式不灵活：固定的表结构，灵活度稍欠;

#### 非关系型数据库

##### 特点

- 非关系型数据库严格上不是一种数据库，应该是一种数据结构化存 储方法的集合，可以是文档或者键值对等。不支持事务一致特性。

##### 优点

- 格式灵活：存储数据的格式可以是key,value形式、文档形式、图片形式等等；
- 高扩展性：基于键值对，数据没有耦合性，容易扩展；
- 速度快：无需经过SQL层的解析，读写性能很高；

##### 缺点

- 不支持SQL：不提供SQL支持，学习和使用成本较高；
- 不支持事务：无事务处理能力；
- 不支持复杂查询：数据结构相对复杂，复杂查询方面稍欠；



## Oracle入门

### 什么是Oracle数据库

所有的关系型数据库存储数据的集合就是磁盘中的文件。Oracle数据库其实就是一组文件的集合。Oracle 数据库分别由：数据文件、控制文件、日志文件所构成。

#### 数据文件(.DBF)

数据文件是一个二进制文件，是用于保存用户应用程序数据和Oracle系统内部数据的文件，这些文件在操作系统中就是普通的操作系统文件。Oracle在创建表空间的同时会创建数据文件。

#### 控制文件(.CTL)

控制文件是一一个二进制文件，它主要记录数据库的名称、数据库的数据文件存放位置等信息。一个控制文件只能属于一个数据库。如果控制文件丢失，这数据库就无法操作。

#### 日志文件（.LOG)

日志文件在Oracle数据库中分为重做日志(Redo Log File)文件和归档日志文件两种。重做日志文件是Oracle数据库正常运行不可缺少的文件。重做日志文件主要记录了数据库操作过程。用于备份和还原数据库，以达到数据库的最新状态。

### 什么是 Oracle实例

实例就是数据库启动后分配的内存和建立的后台进程.数据库关闭后，物理上的文件还存在，但实例(分配的内存和建立的进程)就没有了

### Oracle 实例与数据库的关系

实例就是一组操作系统进程 (或者是一个多线程的进程) 以及一些内存。这些进程可以操作数据库；而数据库只是一个文件集合(包括数据文件、临时文件、重做日志文件和控制文件)。
在任何时刻，一个实例只能有一组相关的文件(与-个数据库关联)。大多数情况下，反过来也成立： 一个数据库.上只有一个实例对其进行操作。

### Oracle 版本说明

- Oracle 8i
- Oracle 9i
- Oracle 10g
- Oracle 11g
- Oracle 12c



- I： i代表 Internet 8i 版本开启对Internet的支持。所以，在版本号之后，添加了标识i。
- G： g代表Grid网格。10g 加入了网格计算的功能，因此版本号之后的标识使用了字母g。
- C： c代表云(cloud)计算设计。12c 版本表示对云计算的支持。



## Oracle的安装与卸载

### Oracle安装步骤



### Oracle 卸载步骤

#### 停止使用Oracle的服务

停用oracle服务，进入计算机管理，在服务中，找到oracle开头的所有服务，右击选择停止。

#### 运行卸载Oracle数据库程序

在开始菜单中找到Oracle 安装产品，点击运行Oracle自带的卸载程序Universal Installer工具卸载。

#### 删除使用Oracle的服务

开始菜单中，找到`Universal Installer`，运行`Oracle Universal Installer`，单击卸载产品，在产品清单窗口中，单击全部展开，除了`OraDb11g_home`外，勾选其他项目，单击删除，根据软件提示单击下一步最终完成卸载。

#### 删除注册表中Oracle相关项

在命令窗口，输入`regedit`，打开注册表，依次展开`HKEY_ LOCAL_MACHINE\SOFTWARE`，找到`oracle`，删除之。
依次展开`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`中，删除所有`oracle`开头的项。
依次展开`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog\Application`，删除
所有`oracle`开头的项。
扩展删除(以下不是必须的注册表删除项) ，如果安装不成功可以自己也把这些删除了。在`HKEY_CLASSES_ROOT`，删除以`Ora`、`Oracle`、 `Orcl `或`EnumOra`为前缀的键删除`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\MenuOrder\StartMenu\Programs`中所有以`oracle `开头的键。
删除`HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBCINST.INI`中除`Microsoft ODBC for Oracle`注册表键以外的所有含有`Oracle`的键。

#### 删除Oracle环境变量

右键点击`我的电脑-->属性-->高级-->环境变量`，删除环境变量`ORACLE_HOME`、`TNS_ADMIN`等环境变量，删除`PATH`中等环境变量有关`Oracle`的设定的路径信息。

#### 删除“开始”菜单中Oracle目录

打开资源管理器，在地址栏中输入`%userprofile%\「开始」菜单\程序`回车，删除安装的`Oracle`目录。然后再到地址栏中输入`%allusersprofle%「开始」菜单\程序`回车，删除安装的`Oracle`目录。

#### 重新启动计算机

重启电脑。

#### 删除`Program Files\Orace`目录

如果在`Program Files\Oracle`目录存在，则删除`Program Files\Oracle`目录。

#### 删除Oracle安装目录

删除`Oracle`的安装目录`app`等目录。



## Oracle目录结构与系统用户

### Oracle目录结构

![image-20220821221341366](Oracle_Study.assets/image-20220821221341366.png)

#### admin目录

记录Oracle实例的配置，运行日志等文件。每个实例一个目录。
SID: System IDentifer的缩写，是Oracle实例的唯一标记。 在Oracle中一个实例只能操作一个数据库。如果安装多个库那么就会有多个实例，我们可以通过实例SID来区分。由于Oracle中一个实例只能操作一个数据库的原因oracle中也会使用SID来作为库的名称。

#### cfgtoollogs目录

下面子目录分别存放当运行`dbca`, `emca`, `netca `等图形化配置程序时的`log`。

#### checkpoints目录

存放检查点文件

#### diag目录

Oracle11g新添加的一个重组目录。其中的子目录，基本上Oracle每个组件都有了自己单独的目录，在Oracle10g中我们一直诟病的log文件散放在四处的问题终于得到解决，无论是`asm`还是`crs`还是`rdbms `，所有组件需要被用来诊断的log文件都存放在了这个新的目录下。

#### flash_recovery_area(闪回区)目录

闪回区：分配一个特定的目录位置来存放一些特定的恢复文件，用于集中和简化管理数据库恢复工作。闪回区可存储完全的数据文件备份、增量备份、数据文件副本、当前的控制文件、备份的控制文件、spfile 文件、快照控制文件、联机日志文件、归档日志、块跟踪文件、闪回日志。

#### oradata目录

存放数据文件。

##### orcl数据库文件

![image-20220822031749672](Oracle_Study.assets/image-20220822031749672.png)

#### 数据库中的文件介绍

- CONTROLO1.CTL

  - Oracle数据库的控制文件。

- EXAMPLE01.DBF

  - Oracle数据库表空间文件。

- REDO01.LOG

  - Oracle数据库的重做日志文件。

- SYSAUX01.DBF

  - 11g新增加的表空间。主要存储除数据字典以外的其他数据对象。由系统内部自动维护。

- SYSTEM01.DBF

  - 用于存放Oracle系统内部表和数据字典的数据。比如，表名、列名、用户名等。

- TEMP01.DBF

  - 临时表空间文件。

- UNDOTBSO1.DBF

  - 撤销表空间文件。用来保存回滚数据。

- USERSO1.DBF

  - 用户表空间。

#### product目录

Oracle RDBMS的软件存放目录。RDBMS即关系数据库管理系统(Relational Database
Management System)。

### Oracle系统用户

#### sys用户

sys: sys是Oracle中的超级账户，拥有的权限最大。可以完成数据库的所有管理任务。

#### system用户

system:没有sys权限大，通常用来创建一些用户查看管理信息的表或视图。不建议使用system用户来创建一些与管理无关的表或者视图。

#### 二者在登录时的区别

sys和system在登录Oracle时， sys只能以系统管理员(sysdba)或系统操作员(sysoper)的权限登录，而system可以直接登录(normal)。

#### scott用户

scott :是oracle 提供的示例用户，提供了一些学习 oracle 操作的数据表。如: emp、dept、salgrade、bonus 表

### Oracle 的启动与关闭

#### Oracle启动

Oracle是通过系统的服务来启动的。

##### `OracleServiceORCL`(必须启动)

`OracleServiceORCL`:数据库服务(数据库实例)，是Oracle核心服务该服务，是数据库启动的基础，只有该服务启动，Oracle 数据库才能正常启动。

##### `OracleOraDb11g_home1TNSListener`(必须启动)

`OracleOraDb11g_horme1TNSListener`:监听器服务，服务只有在数据库需要远程访问的时候或者使用PLSQL Developer 等第三方工具时才需要。.

##### Oracle ORCL VSS Writer Service(非必须启动)

Oracle ORCL VSS Writer Service: Oracle 卷映射拷贝写入服务，VSS(Volume Shadow Copy Service)能够让存储基础设备(此如磁盘，阵列等)创建高保真的时间点映像，即映射拷贝(shadow copy)。 它可以在多卷或者单个卷上创建映射拷贝，同时不会影响到系统的系统能。

##### `OracleDBConsoleorcl`(非必须启动)

`OracleDBConsoleorcl` : Oracle 数据库控制台服务， orcl 是Oracle的实例标识，默认的实例为`orcl`。 在运行Enterprise Manager(企业管理器 OEMD的时候，需要启动这个服务。

##### `OracleJobSchedulerORCL`(非必须启动)

`OracleJobSchedulerORCL`: Oracle 作业调度(定时器)服务， ORCL是Oracle实例标识。

##### `OracleMTSRecoveryService`(非必须启动)

`OracleMTSRecoveryService`:服务端控制。该服务允许数据库充当-个微软事务服务器MTS、COM/COM+对象和分布式环境下的事务的资源管理器。

#### Oracle 关闭

关闭Oracle只需要将服务停止即可。

### Oracle客户端工具介绍

#### Oracle自带客户端工具SQL Plus

![image-20220822034533588](Oracle_Study.assets/image-20220822034533588.png)

![image-20220822034754159](Oracle_Study.assets/image-20220822034754159.png)

sys用户登录命令: `sys as sysdba | sysoper`
system用户登录命令: system

#### Oracle 第三方工具PL/SQL Developer

##### 安装PL/SQL Developer

![image-20220822035056872](Oracle_Study.assets/image-20220822035056872.png)

![image-20220822035136647](Oracle_Study.assets/image-20220822035136647.png)

![image-20220822035220439](Oracle_Study.assets/image-20220822035220439.png)

![image-20220822035326254](Oracle_Study.assets/image-20220822035326254.png)

###### Command Window

![image-20220822035901211](Oracle_Study.assets/image-20220822035901211.png)

###### SQL Window

![image-20220822035843687](Oracle_Study.assets/image-20220822035843687.png)

### Oracle 的使用

#### Oracle 的表空间

##### Oracle的表空间分类

###### 永久表空间

表空间是数据库的逻辑划分,一个表空间只能属于一个数据库。所有的数据库对象都存放在指定的表空间中。但主要存放的是表，所以称作表空间。

###### 临时表空间

Oracle临时表空间主要用来做查询和存放一些缓冲区数据。临时表空间消耗的主要原因是需要对查询的中间结果进行排序。重启数据库可以释放临时表空间。

##### 创建永久表空间命令

````sql
create tablespace 永久表空间名称 datafile '永久表空间物理文件位置' size 15M autoextend on next 10M permanent online;
````

#### 创建用户

##### 通过PL/SQL Developer 工具创建用户
