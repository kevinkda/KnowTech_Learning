#! /usr/bin/sh
# create kibana

TRUE="true"
FALSE="false"

USE_VERSION="7.12.1"
AUTO_MKDIR_DIR=""
DIR_AUTH_CODE=777
SERVICE_NAME_PREFIX="kibana"
IMAGE_NAME="kibana"

ENABLE_DELETE_HISTORY_DIR=${FALSE}
ENABLE_AUTO_MAKE_DIR=${FALSE}


cd `dirname $0`
work_dir=`pwd`
echo "Current Dir Path: ${work_dir}"


serviceName="${SERVICE_NAME_PREFIX}"
dirList=(${AUTO_MKDIR_DIR//,/})


function build() {
    docker run --name "${serviceName}" \
    -p 5601:5601 \
    -v "${work_dir}/kibana.yml:/usr/share/kibana/config/kibana.yml" \
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

