#!/bin/sh
# Author：Alan Huang
# Description: OpenVPN管理

cd $(dirname $0)
WORK_DIR=$(pwd)
THIS_SCRIPT_NAME=$(basename $0)
FILE_PATH=${2}
lOG_PATH=${WORK_DIR}/log/openvpn.log
SERVICE_NAME="OpenVPN"

echo "Current Dir Path: ${WORK_DIR}"

PID_DIR="${WORK_DIR}/pid"
PID="${PID_DIR}/${SERVICE_NAME}.pid"

# Check that the program is running
is_exist() {
  pid=$(ps -ef | grep ${SERVICE_NAME} | grep -v grep | awk '{print $2}')
  # Returns 1 if it does not exist and 0 if it exists
  if [ -z "${pid}" ]; then
    return 1
  else
    return 0
  fi
}

start() {
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> runing PID = " ${pid} "<<<"
  else
    openvpn --daemon --cd ${WORK_DIR}/client --config ${FILE_PATH} --log-append ${lOG_PATH}
  fi
  echo $! >${PID}
  echo ">>> Start " ${SERVICE_NAME} " successed, PID = $! <<<"
  echo ">>> Log Path: ${LOG_PATH} <<<"
}

stop() {
  # is_exist
  pidf="$(cat ${PID})"
  # echo "$pidf"
  echo ">>> ${SERVICE_NAME} PID = ${pidf} Begin Kill ${pidf} <<<"
  kill "${pidf}"
  rm -rf "${PID}"
  sleep 2
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${SERVICE_NAME} 2 PID = $pid Begin Kill -9 $pid  <<<"
    kill -9 ${pid}
    sleep 2
    echo ">>> ${SERVICE_NAME} Process Stopped <<<"
  else
    echo ">>> ${SERVICE_NAME} is not running <<<"
  fi
}

restart() {
  stop
  start
}

status() {
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${SERVICE_NAME} is running PID is ${pid} <<<"
  else
    echo ">>> ${SERVICE_NAME} is not running <<<"
  fi
}

disable() {
  echo "No such function"
}

enable() {
  echo "No such function"
}

showLog() {
  tail -f "${LOG_PATH}"
}

help() {
  echo "OpenVPN 服务管理"
  echo "Usage: manage.sh [ stop | start | status | restart | disable | enable | log ]"
}

case "$1" in
"start")
  start
  ;;
"stop")
  stop
  ;;
"restart")
  restart
  ;;
"status")
  status
  ;;
"disable")
  disable
  ;;
"enable")
  enable
  ;;
"log")
  showLog
  ;;
"help")
  help
  ;;
*)
  help
  ;;
esac
exit 0
