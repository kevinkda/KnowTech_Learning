# Oracle数据库Docker镜像制作

[toc]

## 相关网址

[oracle/dockerimages](https://github.com/oracle/docker-images)



## 流程

### 下载

1. 首先先前往[官网下载](https://github.com/oracle/docker-images)docker-images

### 上传

1. 将下载的docker-images中的OracleDatabase目录上传至linux上
   1. OracleDatabase目录下的RAC应该是集群
   2. SingleInstance是单节点
   3. 根据需求进入对应目录中的dockerfiles目录下

### 讲解

1. dockerfiles目录下包含了`11.2.0.2`  `12.1.0.2`  `12.2.0.1`  `18.3.0`  `18.4.0`  `19.3.0`  `21.3.0`  七个Oracle版本的文件夹

1.  `buildContainerImage.sh` 用于构建镜像的脚本

   1. 执行 `.buildContainerImage.sh -h` 可以看到他的帮助文档，或者前往[官网](https://github.com/oracle/docker-images/tree/main/OracleDatabase/SingleInstance)

   2. ```tex
      每个目录对应不通的版本，将你从官网下载的oracle版本放入到对应的目录，然后按照buildContainerImage.sh脚本的帮助文档 执行对应的命令和添加对应的参数
      
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
      

### 躲坑

![img](https://img-blog.csdnimg.cn/c704d6b51b894fd9863373e5c4eb76f2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl1ZG9uZ3lhbmcxMjM=,size_20,color_FFFFFF,t_70,g_se,x_16)

1. 第一个红圈说明了在执行 `buildContainerImage.sh` 脚本来构建每个版本的镜像时跟的参数，比如11g是-x，12c可以是-e也可以是-s

2. 第二个红圈要特别注意，需要将下载下来额Oracle包的名字改成 `linuxx64_<version>_database.zip` 这种格式，19c不需要，直接在官网下载 `Linux x86-64` 这个版本就ok，但是12c和11g不一样，如果遇到下载下来的包名字不对或者在执行脚本时报错找不到包，则需要仔细核查包名字然后修改

3. 其中 18c XE 和 21c XE 的不用下载镜像，其余版本都需要自行下载镜像

4. 11g的版本不能用 `linuxx64_<version>_database.zip` 这种格式的包，而是需要 `oracle-xe-11.2.0-1.0.x86_64.rpm.zip` 这个格式的包。

5. 以上关于 `包名字` 相关的都可以进入 `每个版本文件夹` 下，然后去查看其中的 `DockerFile` 文件

   ![img](https://img-blog.csdnimg.cn/ab710b0f2296451899669dd5b785f605.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAbGl1ZG9uZ3lhbmcxMjM=,size_20,color_FFFFFF,t_70,g_se,x_16)

### 提醒

1. oracle11g 需要的是 oracle-xe-11.2.0-1.0.x86_64.rpm.zip 这个安装包。

2. 在镜像制作完成后 docker run的时候 要加上 --shm-size="2g" 来设置容日的内存，如果不设置可能会导致容器启动失败

3. sqlplus 出现 `ORA-12547: TNS:lost contact`

   执行 `chmod 6751 $ORACLE_HOME/bin/*`