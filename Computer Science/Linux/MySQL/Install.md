# MySQL Install

[TOC]

## RHEL / CentOS

### RHEL / CentOS 7

1. Install `Noarch`

   ```shell
   yum install ./mysql80-community-release-el7-3.noarch.rpm
   ```

2. Install RPM

   ```shell
   yum install ./mysql*
   ```

   Install List

   - mysql-community-clien
   - mysql-community-client-plugins
   - mysql-community-common
   - mysql-community-devel
   - mysql-community-embedded-compat
   - mysql-community-libs
   - mysql-community-libs-compat
   - mysql-community-server
   - mysql-community-test

3. MySQL Fixed Parameter Configuration

   1. View The Case Sensitive Configuration Of Current MySQL

      ```mysql
      show global variables like '%lower_case%';
      ```

   2. Case Sensitive Configuration

      [linux 下 设置 MySQL8 表名大小写不敏感方法，解决设置后无法启动 MySQL 服务的问题](https://www.cnblogs.com/czwbig/p/9961069.html)

   3. Modify Default Character Set

   ```cnf
   # /etc/my.cnf
   lower_case_table_names = 0 # Sensitive
   lower_case_table_names = 1 # Insensitive
   character_set_server=utf8mb4
   
   [client]
   default-character-set=utf8mb4
   ```

   Path: `/etc/my.cnf`

   ```cnf
   # For advice on how to change settings please see
   # http://dev.mysql.com/doc/refman/8.0/en/server-configuration-defaults.html
   
   [mysqld]
   #
   # Remove leading # and set to the amount of RAM for the most important data
   # cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
   # innodb_buffer_pool_size = 128M
   #
   # Remove the leading "# " to disable binary logging
   # Binary logging captures changes between backups and is enabled by
   # default. It's default setting is log_bin=binlog
   # disable_log_bin
   #
   # Remove leading # to set options mainly useful for reporting servers.
   # The server defaults are faster for transactions and fast SELECTs.
   # Adjust sizes as needed, experiment to find the optimal values.
   # join_buffer_size = 128M
   # sort_buffer_size = 2M
   # read_rnd_buffer_size = 2M
   #
   # Remove leading # to revert to previous value for default_authentication_plugin,
   # this will increase compatibility with older clients. For background, see:
   # https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_authentication_plugin
   # default-authentication-plugin=mysql_native_password
   
   datadir=/var/lib/mysql
   socket=/var/lib/mysql/mysql.sock
   
   log-error=/var/log/mysqld.log
   pid-file=/var/run/mysqld/mysqld.pid
   
   lower_case_table_names=1
   character_set_server=utf8mb4
   
   [client]
   default-character-set=utf8mb4
   ```

4. System Configuration

   1. System Service Configuration

      ```shell
      # Start mysqld Service
      systemctl start mysqld.service
      
      # Set Startup And Self Startup
      systemctl enable mysqld.service
      # If the boot does not start
      systemctl daemon-reload
      
      # Start mysqld Service
      systemctl start mysqld.service
      # Stop mysqld Service
      systemctl stop mysqld.service
      # Restart mysqld Service
      systemctl restart mysqld.service
      ```

   2. Open Firewall

      ```shell
      # 查看已经开放的端口
      firewall-cmd --list-ports
      # 开启端口
      firewall-cmd --zone=public --add-port=3306/tcp --permanent
      # 重启Firewall
      firewall-cmd --reload
      # 停止Firewall
      systemctl stop firewalld.service
      # 禁止Firewall开机启动
      systemctl disable firewalld.service
      ```

5. Configuration And Parameter Query In MySQL Database

   1. Get The Initial Login Password Of The `root` Account MySQL

      ```shell
      cat /var/log/mysqld.log | grep password
      ```

   2. `root` Account Remote Permissions

      ```mysql
      # 远程设置
      use mysql;
      update user set host='%' where user='root';
      # 授权用户名的权限，赋予任何主机访问数据的权限
      GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'WITH GRANT OPTION;
      FLUSH PRIVILEGES;

   3. View Database Parameters

      ```mysql
      # 查看数据库编码
      show variables like 'character%';
      SHOW VARIABLES WHERE Variable_name LIKE 'character_set_%' OR Variable_name LIKE 'collation%';
      
      # 查看慢查询日志是否开启以及日志位置
      show variables like 'slow_query%';
      # 查看慢查询日志超时记录时间
      show variables like 'long_query_time';
      
      # 查询mysql最大连接数设置
      show global variables like 'max_conn%';
      SELECT @@MAX_CONNECTIONS AS 'Max Connections';
      # 查看最大链接数
      show global status like 'Max_used_connections';
      # 查看链接创建以及现在正在链接数
      show status like 'Threads%';
      # 查看数据库当前链接
      show processlist;
      # 查看数据库配置
      show variables like '%quer%';
      
      #查看mysql版本：
      select version();
      ```

   4. 

