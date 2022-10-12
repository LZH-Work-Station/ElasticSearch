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
  while [ "$begin_date" -le "$end_date" ]; do
    year=${begin_date:0:4}
    month=${begin_date:4:2}
    day=${begin_date:6:2}
    begin_date=$(date -d "${begin_date}+1days" +%Y%m%d)
    python3.6 $PARENT_DIR/core/todayPriceApplication.py $year-$month-$day
    wait
    python3.6 $PARENT_DIR/core/IntraDayPriceApplication.py $year-$month-$day
    wait
  done
fi

if [ $# -eq 1 ]; then
  date=$1
  year=${date:0:4}
  month=${date:4:2}
  day=${date:6:2}
  python3.6 "$PARENT_DIR"/core/todayPriceApplication.py $year-$month-$day
  wait
  python3.6 "$PARENT_DIR"/core/IntraDayPriceApplication.py $year-$month-$day
  wait
fi

if [ $# -eq 0 ]; then
  python3.6 "$PARENT_DIR"/core/todayPriceApplication.py $YESTERDAY
  wait
  python3.6 "$PARENT_DIR"/core/IntraDayPriceApplication.py $YESTERDAY
  wait
fi
