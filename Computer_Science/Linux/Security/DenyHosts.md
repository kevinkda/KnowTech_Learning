# DenyHosts

[TOC]

## 下载路径

[DenyHosts GitHub Releases](https://github.com/denyhosts/denyhosts/releases)

- [ZIP](https://github.com/denyhosts/denyhosts/archive/refs/tags/v3.0.zip)
- [TAR](https://github.com/denyhosts/denyhosts/archive/refs/tags/v3.0.tar.gz)



## 安装方法

```shell
cd /opt
# 下载程序源码
wget https://github.com/denyhosts/denyhosts/archive/refs/tags/v3.0.zip -O denyhosts.zip

# 解压
unzip denyhosts.zip

# 移动至默认工作目录
mv /opt/denyhosts /usr/share

cd /usr/share/denyhosts
# 程序源码编译&安装
python setup.py install

# 建立软链接
rm -rf /etc/denyhosts.conf
ln -s /usr/share/denyhosts/denyhosts.conf /etc/denyhosts.conf
ln -s /usr/share/denyhosts/denyhosts.py /usr/sbin/denyhosts
# 设置开机自动启动
ln -s /usr/share/denyhosts/denyhosts.service /usr/lib/systemd/system/
systemctl enable denyhosts.service
```



## 启动命令

```shell
# 启动DenyHosts
daemon-control start 
# 查看DenyHosts启动状态
daemon-control status  
# 停止DenyHosts
daemon-control stop    
```



## 配置

配置文件中配置了一些文件的路径，启动过程中可能存在如下错误。手动为其建立目录。

```shell
Can't read: /var/log/auth.log
[Errno 2] No such file or directory: '/var/log/auth.log'
Error deleting DenyHosts lock file: /var/run/denyhosts.pid
[Errno 2] No such file or directory: '/var/run/denyhosts.pid'
```

安装完成后，DenyHosts会被装到`/usr/lib/python2.7/site-packages/DenyHosts`下。

在启动的时候，python2会报如下错误：

```python
Traceback (most recent call last):
  File "/usr/sbin/denyhosts", line 229, in <module>
    first_time, noemail, daemon, foreground)
  File "/usr/lib/python2.7/site-packages/DenyHosts/deny_hosts.py", line 77, in __init__
    offset = self.process_log(logfile, last_offset)
  File "/usr/lib/python2.7/site-packages/DenyHosts/deny_hosts.py", line 488, in process_log
    self.__report.add_section(msg, new_denied_hosts)
  File "/usr/lib/python2.7/site-packages/DenyHosts/report.py", line 41, in add_section
    if type(i) in (TupleType, ListType):
NameError: global name 'TupleType' is not defined

DenyHosts exited abnormally
```

解决方法是打开：`/usr/lib/python2.7/site-packages/DenyHosts/report.py`，将第5行代码的注释去掉，重启DenyHosts。

```python
# from types import ListType, TupleType
```



## 参考

- [DenyHosts——对抗ssh暴力破解](https://zhuanlan.zhihu.com/p/355514144)
- [DenyHosts安装及配置](https://www.jianshu.com/p/953b40e234dc)
- [DenyHosts](http://denyhosts.sourceforge.net/faq.html)
- [DenyHosts安装及配置详解](https://www.jianshu.com/p/59ffb6adc37c)