#! /bin/sh
# Author: AlanHuang
# Description: Copy the configuration file in logstash to the local

id=${1}

sudo docker cp ${id}:/usr/share/logstash/config /mnt/remote/data/elastic/logstash_02
sudo docker cp ${id}:/usr/share/logstash/data /mnt/remote/data/elastic/logstash_02
sudo docker cp ${id}:/usr/share/logstash/modules /mnt/remote/data/elastic/logstash_02
sudo docker cp ${id}:/usr/share/logstash/pipeline /mnt/remote/data/elastic/logstash_02
sudo docker cp ${id}:/usr/share/logstash/tools /mnt/remote/data/elastic/logstash_02
sudo docker cp ${id}:/var/log /mnt/remote/data/elastic/logstash_02/log
