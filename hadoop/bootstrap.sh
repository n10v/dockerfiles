#!/bin/bash

: ${HADOOP_PREFIX:=/usr/local/hadoop}

$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh

rm -f /tmp/*.pid

service ssh start
$HADOOP_PREFIX/sbin/start-dfs.sh

if [[ $1 == "-d" ]]; then
    while true; do sleep 1000; done
fi

if [[ $1 == "-bash" ]]; then
		/bin/bash
fi
