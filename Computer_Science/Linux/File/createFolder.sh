#!/bin/bash
# Author: AlanHuang
# Description: 批量创建文件夹

path=${1}
prefix=${2}
dic=(
    [1]='100' 
    [2]='200'
    [3]='300'
    )

for names in $(echo ${!dic[*]}); do
    mkdir ${path}/${prefix}-${names} && cd ${path}/${prefix}-${names} && mkdir in out err
done