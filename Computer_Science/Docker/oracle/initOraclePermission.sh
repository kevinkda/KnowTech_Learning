#! /bin/sh
groupadd -g 54321 oinstall
groupadd -g 54322 dba
groupadd -g 54323 oper
groupadd -g 54324 backupdba
groupadd -g 54325 dgdba
groupadd -g 54326 kmdba
groupadd -g 54330 racdba

useradd oracle -u 54321 -G oinstall,dba,oper,backupdba,dgdba,kmdba,racdba

chown 54321.54321 oradata scripts