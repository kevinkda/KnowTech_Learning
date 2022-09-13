#!/bin/sh
#bulk rename
#2022/7/23
# English Documentation
# 1. % sign interception, delete the right character, keep the left character
# 2. %% sign interception, delete the right character, keep the left character
# 3. # Intercept, delete the characters on the left, and keep the characters on the right.
# 4. ## sign interception, delete the left character, keep the right character
# Chinese Documentation
# 1. % 符号截取，删除右边字符，保留左边字符
# 2. %% 符号截取，删除右边字符，保留左边字符
# 3. # 截取，删除左边的字符，保留右边的字符。
# 4. ## 符号截取，删除左边字符，保留右边字符

CHOOSE=${1}
CUT=${2}

name=GS53YNCKTX2020

if [ ${CHOOSE} -eq 1 ] 
then
  for name in `ls *`;
  do 
   mv $name ${name} ${name#${CUT}${name}};
  done
elif [ ${CHOOSE} -eq 2 ]  
then
  for name in `ls *IVLT*`;
  do  
    mv $name abc${name%${CUT}*};
  done
else
  echo 'no this choose'
fi


