#!/bin/bash

PARENT_DIR=$(
  cd $(dirname $0)
  cd ..
  pwd
)
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)

if [ $# -eq 3 ]; then
  begin_date=$1
  end_date=$2
  while [ "$begin_date" -le "$end_date" ]; do
    year=${begin_date:0:4}
    month=${begin_date:4:2}
    day=${begin_date:6:2}
    begin_date=$(date -d "${begin_date}+1days" +%Y%m%d)
    echo $3
    python3.6 $PARENT_DIR/core/$3 $year-$month-$day
  done
fi

if [ $# -eq 0 ]; then
  date=$YESTERDAY
  year=${date:0:4}
  month=${date:4:2}
  day=${date:6:2}
  python3.6 $PARENT_DIR/bin/rollBackDailyPrice.py $year-$month-$day $year-$month-$day
  python3.6 $PARENT_DIR/bin/rollBackIntradayPrice.py $year-$month-$day $year-$month-$day
fi
