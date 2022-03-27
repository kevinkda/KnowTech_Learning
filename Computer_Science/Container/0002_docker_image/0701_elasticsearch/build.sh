#! /usr/bin/sh
# create elasticsearch

TRUE="true"
FALSE="false"

USE_VERSION="7.12.1"
AUTO_MKDIR_DIR="data,logs,plugins"
DIR_AUTH_CODE=777
SERVICE_NAME_PREFIX="elasticsearch"
IMAGE_NAME="elasticsearch"

ENABLE_DELETE_HISTORY_DIR=${FALSE}
ENABLE_AUTO_MAKE_DIR=${TRUE}


cd `dirname $0`
work_dir=`pwd`
echo "Current Dir Path: ${work_dir}"


serviceName="${SERVICE_NAME_PREFIX}"
dirList=(${AUTO_MKDIR_DIR//,/})


function build() {
    docker run --name "${serviceName}" \
    -p 9200:9200 \
    -p 9300:9300 \
    -v "${work_dir}/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml" \
    -v "${work_dir}/data:/usr/share/elasticsearch/data" \
    -v "${work_dir}/plugins:/usr/share/elasticsearch/plugins" \
    -v "${work_dir}/logs:/usr/share/elasticsearch/logs" \
    -e ES_JAVA_OPTS="-Xms256m -Xmx256m" \
    -e "discovery.type=single-node" \
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
