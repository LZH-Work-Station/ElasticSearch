#!/bin/bash

PARENT_DIR=$(
  cd $(dirname $0)
  cd ..
  pwd
)
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)

if [ $# -eq 2 ]; then
  begin_date=$1
  end_date=$2
  python3.6 $PARENT_DIR/bin/rollBackDailyPrice.py $begin_date $end_date;
  python3.6 $PARENT_DIR/bin/rollBackIntradayPrice.py $begin_date $end_date;
fi

if [ $# -eq 0 ]; then
  python3.6 $PARENT_DIR/bin/rollBackDailyPrice.py $YESTERDAY $YESTERDAY;
#  python3.6 $PARENT_DIR/bin/rollBackIntradayPrice.py $YESTERDAY $YESTERDAY;
fi
