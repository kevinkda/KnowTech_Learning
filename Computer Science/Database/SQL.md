# SQL Learning

[TOC]

本笔记为阿里云天池龙珠计划SQL训练营的学习内容，链接为：https://tianchi.aliyun.com/specials/promotion/aicampsql



## DBMS

DBMS 主要通过数据的保存格式（数据库的种类）来进行分类，现阶段主要有以下 5 种类型.

- 层次数据库（Hierarchical Database，HDB）

- 关系数据库（Relational Database，RDB）

  > 这种类型的 DBMS 称为关系数据库管理系统（Relational Database Management System，RDBMS）。比较具有代表性的 RDBMS 有如下 5 种。

  - Oracle Database：甲骨文公司的RDBMS

  - SQL Server：微软公司的RDBMS

  - DB2：IBM公司的RDBMS

  - PostgreSQL：开源的RDBMS

  - MySQL：开源的RDBMS

- 面向对象数据库（Object Oriented Database，OODB）
- XML数据库（XML Database，XMLDB）
- 键值存储系统（Key-Value Store，KVS），举例：MongoDB

### RDBMS

使用 RDBMS 时，最常见的系统结构就是客户端 / 服务器类型（C/S类型）这种结构（图 1-3）

![img](SQL.assets/O1CN01kROUDI22ITX6Evayf_!!6000000007097-0-tps-567-333.jpg)

#### DDL

Data Definition Language，数据定义语言，用来创建或者删除存储数据用的数据库以及数据库中的表等对象。DDL 包含以下几种指令。

- CREATE ： 创建数据库和表等对象
- DROP ： 删除数据库和表等对象
- ALTER ： 修改数据库和表等对象的结构

 

#### DML

Data Manipulation Language，数据操纵语言，用来查询或者变更表中的记录。DML 包含以下几种指令。

- SELECT ：查询表中的数据
- INSERT ：向表中插入新数据
- UPDATE ：更新表中的数据
- DELETE ：删除表中的数据

#### DCL

Data Control Language，数据控制语言，用来确认或者取消对数据库中的数据进行的变更。除此之外，还可以对 RDBMS 的用户是否有权限操作数据库中的对象（数据库表等）进行设定。DCL 包含以下几种指令。

- COMMIT ： 确认对数据库中的数据进行的变更
- ROLLBACK ： 取消对数据库中的数据进行的变更
- GRANT ： 赋予用户操作权限
- REVOKE ： 取消用户的操作权限
