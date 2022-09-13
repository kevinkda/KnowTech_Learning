#!/bin/bash

# Author: AlanHuang
# Description:此脚本用于每个月自动更新kibana索引
#   操作类型分为add和delete
#   每月1号凌晨3点执行
#   所有elasticsearch中的索引写入type_log.txt文件中，
#   然后顺序取出并创建kibana索引。如果新增索引，
#   可直接写入type_log.txt并执行脚本即可。
#   对已经存在的索引不会存在影响。

# add or del
action=add
logst_url='/mnt/remote/data/elastic/logstash_02/script'

URL="http://localhost:5601"
# 每当有新的,从type_log.txt文件中读取所有索引的type
# index_pattern = ""
# ID=index_pattern
domain_name_file=${logst_url}/type_log.txt

time_field='@timestamp'
#date=`date +%Y-%m`
date=2022-06

# 更新日志
log_file=${logst_url}/update_index.log
echo "${date}" >>${log_file}

#中间文件，用来存放type_log.txt中有用的行和其行号
middle_file=${logst_url}/middle.txt
grep -E -n '^[[:alnum:]]' ${domain_name_file} >${middle_file}

domain_name_num=$(wc -l ${middle_file} | awk '{print $1}')
for ((i = 1; i <= ${domain_name_num}; i++)); do
  domain_name_type=$(sed -n "${i}p" ${middle_file} | awk -F':' '{print $2}')
  ###开始新增新的索引
  if [ $action == "add" ]; then
    curl -f -XPOST -H 'Content-Type: application/json' -H 'kbn-xsrf: anything' \
      "${URL}/api/saved_objects/index-pattern/logstash-app_${domain_name_type}_${date}" -d"{\"attributes\":{\"title\":\"logstash-app_${domain_name_type}_${date}\",\"timeFieldName\":\"@timestamp\"}}" >>${log_file}
  elif [ $action == "del" ]; then
    curl -XDELETE "${URL}/api/saved_objects/index-pattern/logstash-app_${domain_name_type}_${date}" -H 'kbn-xsrf: true' >/dev/null
  else
    echo "action errror" >>${log_file}
    exit 100
  fi

  #对每一条操作都进行日志记录，这样每月凌晨执行完成后，可过滤日志文件，将错误发送给集群负责人。
  if [ $? -eq 0 ]; then
    echo "success ${domain_name_type}" >>${log_file}
  else
    echo "error ${domain_name_type}" >>${log_file}
  fi
done

#添加默认索引
curl -f -XPOST -H 'Content-Type: application/json' -H 'kbn-xsrf: anything' ${URL}/api/kibana/settings/defaultIndex -d "{\"value\":\"logstash-app_www_${date}\"}" >>${log_file}

mv -f ${logst_url}/middle.txt /tmp/
