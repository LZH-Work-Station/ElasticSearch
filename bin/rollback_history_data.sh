#!/bin/bash

PARENT_DIR=$(
  cd $(dirname $0)
  cd ..
  pwd
)

if [ $# -eq 2 ]; then
  begin_date=$1
  end_date=$2
  while [ "$begin_date" -le "$end_date" ]; do
    year=${begin_date:0:4}
    month=${begin_date:4:2}
    day=${begin_date:6:2}
    begin_date=$(date -d "${begin_date}+1days" +%Y%m%d)
    sh $PARENT_DIR/bin/executor.sh $year-$month-$day $1 $2 todayPriceApplication.py &
    sh $PARENT_DIR/bin/executor.sh $year-$month-$day $1 $2 intraDayPriceApplication.py
  done
fi
