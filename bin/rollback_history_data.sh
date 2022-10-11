#!/bin/bash

if [ $# -eq 2 ]; then
  begin_date=$1
  end_date=$2
  while [ "$begin_date" -le "$end_date" ]; do
    year=${begin_date:0:4}
    month=${begin_date:4:2}
    day=${begin_date:6:2}
    begin_date=$(date -d "${begin_date}+1days" +%Y%m%d)
    python3.6 core/todayPrice.py $year-$month-$day
  done
fi

if [ $# -eq 1 ]; then
  date=$1
  year=${date:0:4}
  month=${date:4:2}
  day=${date:6:2}
  python3.6 core/todayPrice.py $year-$month-$day
fi

if [ $# -eq 0 ]; then
  echo "No args error"
fi
