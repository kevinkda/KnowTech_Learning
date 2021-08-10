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

3. Case Sensitive Configuration

   ```shell
   # /etc/my.cnf
   lower_case_table_names = 0 # Sensitive
   lower_case_table_names = 1 # Insensitive
   ```

4. System Service Configuration

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

5. 

   1. `root` Account Remote Permissions

