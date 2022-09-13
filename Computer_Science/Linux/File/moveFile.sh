#!/bin/sh
#Author: AlanHuang
#Date: 2022-7-18
#Description: Move the file on the specified date to the specified directory
DATE=${1}

FILE_PATH_1=/opt
FILE_PATH_2=/tmp
for FILE in $(find -maxdepth 1 -newermt ${DATE} );do
    if [[ $FILE == *HM* ]]; then
        echo "Move file "$FILE" to "${FILE_PATH_1}
        cp $FILE ${FILE_PATH_1}
    elif [[ $FILE == *VS* ]]; then
        echo "Move file "$FILE" to "${FILE_PATH_2}
	    cp $FILE ${FILE_PATH_2}
    else
        echo "This file is not a file that needs to be moved: "$FILE
    fi
done
