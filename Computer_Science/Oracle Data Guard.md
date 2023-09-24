**步骤 1：准备 Docker 环境**

1. 安装 Docker：首先，您需要安装 Docker 并确保其正常运行。

2. 获取 Oracle 镜像：在 Docker Hub 或 Oracle 官方网站上获取 Oracle 数据库的 Docker 镜像。这些镜像通常包含预配置的 Oracle 数据库。

**步骤 2：创建主数据库容器**

1. 使用 Oracle 镜像创建主数据库容器，按照所需配置设置数据库参数和环境。

2. 配置主数据库：在容器内运行 SQL*Plus 或其他管理工具，进行数据库配置，启用归档模式等。
    SHUTDOWN IMMEDIATE;
    STARTUP MOUNT;
    ALTER DATABASE ARCHIVELOG;
    ALTER DATABASE OPEN;

3. 生成备份：创建主数据库的备份，以备后续用于初始化备用数据库。
    RMAN   进入rman工具
    CONNECT TARGET /    or   CONNECT TARGET username/password@connect_string   连接目标数据库
    BACKUP DATABASE;   全量备份
    BACKUP DATABASE TO '/backup_dir';  保存到指定目录
    BACKUP DATABASE TO BACKUPSET;   保存到备份集

**步骤 3：创建备用数据库容器**

1. 使用 Oracle 镜像创建备用数据库容器。确保使用相同版本的 Oracle 镜像，并按需设置数据库参数和环境。

2. 配置备用数据库：同样，在备用数据库容器内运行 SQL*Plus 或其他工具，配置必要的初始化参数，例如数据库名、SID、监听器信息等。
    ALTER SYSTEM SET DB_NAME = 'env_02' SCOPE=SPFILE;  指定备用数据库的数据库名。
    ALTER SYSTEM SET DB_UNIQUE_NAME = 'env_02_sync' SCOPE=SPFILE;  指定备用数据库的唯一数据库名。
    ALTER SYSTEM SET INSTANCE_NAME = 'env_02_sync' SCOPE=SPFILE;  指定备用数据库实例的名称。
    ALTER SYSTEM SET REMOTE_LISTENER = '172.100.0.10:1521' SCOPE=SPFILE;  指定主数据库监听器的地址。
    ALTER SYSTEM SET FAL_SERVER = '172.100.0.10:1521' SCOPE=SPFILE;  指定主数据库的 FAL（Fetch Archive Log）服务器地址。

    SELECT DEST_NAME, STATUS, DESTINATION, TYPE FROM V$ARCHIVE_DEST;  查询备用数据库的归档日志传输目标。
    ALTER SYSTEM SET LOG_ARCHIVE_DEST_31 = 'SERVICE=ORCL01 LGWR ASYNC VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) DB_UNIQUE_NAME=ORCL01' SCOPE=SPFILE;  指定备用数据库的归档日志传输目标。


**步骤 4：设置 Docker 网络**

1. 创建 Docker 网络：为了使主数据库容器和备用数据库容器能够通信，您可以创建一个 Docker 网络。

**步骤 5：初始化备用数据库**

1. 在备用数据库容器内，使用主数据库的备份初始化数据库。这将创建备用数据库的初始数据。

**步骤 6：启用备用日志应用**

1. 在备用数据库容器内，使用 SQL*Plus 或其他工具，运行命令启用备用日志应用，使备用数据库可以实时应用主数据库的归档日志。

**步骤 7：测试和监控**

1. 测试切换：模拟主数据库故障，观察备用数据库是否可以自动接管。

2. 监控和维护：确保监控主备数据库状态、同步状态以及定期进行灾难恢复测试。
