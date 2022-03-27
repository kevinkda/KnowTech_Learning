#! /usr/bin/sh
# create nacos

TRUE="true"
FALSE="false"

USE_VERSION="latest"
AUTO_MKDIR_DIR="logs"
DIR_AUTH_CODE=777
SERVICE_NAME_PREFIX="nacos"
IMAGE_NAME="nacos/nacos-server"

ENABLE_DELETE_HISTORY_DIR=${FALSE}
ENABLE_AUTO_MAKE_DIR=${TRUE}


cd `dirname $0`
work_dir=`pwd`
echo "Current Dir Path: ${work_dir}"


serviceName="${SERVICE_NAME_PREFIX}"
dirList=(${AUTO_MKDIR_DIR//,/})


function build() {
    docker  run --name "${serviceName}" \
    -p 8848:8848 \
    --privileged=true \
    -e JVM_XMS=256m \
    -e JVM_XMX=256m \
    -e MODE=standalone \
    -e PREFER_HOST_MODE=hostname \
    -v "${work_dir}/logs:/home/nacos/logs" \
    -v "${work_dir}/application.properties:/home/nacos/conf/application.properties" \
    -d "${IMAGE_NAME}:${USE_VERSION}"
}

function deleteHistoryDir() {
    if [[ ${ENABLE_DELETE_HISTORY_DIR} -eq ${TRUE} ]]; then
        for item in $dirList; do
            echo "Remove History Folder: ${work_dir}/${item}"
            rm "-rf ${item}/"
        done
    fi
}

function dirMakeAndAuth() {
    if [[ ${ENABLE_AUTO_MAKE_DIR} -eq ${TRUE} ]]; then
        echo "Make Dir ${work_dir}/{${AUTO_MKDIR_DIR}}"
        mkdir "-p ${work_dir}/{${AUTO_MKDIR_DIR}}"
        for item in $dirList; do
            echo "Dir Auth ${DIR_AUTH_CODE}, ${work_dir}/${item}"
            chmod "${DIR_AUTH_CODE} ${work_dir}/${item}/"
        done
    fi
}

function auto() {
    deleteHistoryDir
    dirMakeAndAuth
    
    echo "Docker Pull & Run Image: ${IMAGE_NAME}:${USE_VERSION}, Name: ${serviceName}"
    build
}


auto
