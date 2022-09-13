#! /bin/sh
# Author: AlanHuang
# Description: create logstash

docker run -dit --name=logstash \
  --restart=always --privileged=true\
  -e ES_JAVA_OPTS="-Xms512m -Xmx512m" \
  -p 5044:5044 \
  logstash:8.2.2

