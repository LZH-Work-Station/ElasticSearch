#!/bin/bash

PARENT_DIR=$(
  cd $(dirname $0)
  cd ..
  pwd
)

if [ $# -eq 2 ]; then
  sh $PARENT_DIR/bin/executor.sh $1 $2 TodayPriceApplication.py &
  sh $PARENT_DIR/bin/executor.sh $1 $2 IntraDayPriceApplication.py
fi