#!/bin/bash
nohup Xvfb :1 -screen 0 1024x768x24 > /dev/null 2>&1 &
if [ $# -eq 0 ]; then
  INGInious
else
  exec $@
fi
