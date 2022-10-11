#!/bin/bash


if [ $# -eq 2 ]; then
    echo "niu"
fi

if [ $# -eq 1 ]; then
    python3.6 core/todayPrice.py $1
fi

if [ $# -eq 0 ]; then
    begin_date="20160907"
    end_date="20170226"

    while [ "$begin_date" -le "$end_date" ];
    do
        year=${begin_date:0:4}
        week_of_year=$(date -d "$begin_date" +%W)
        echo $year, $week_of_year
        begin_date=$(date -d "${begin_date}+7days" +%Y%m%d)
    done
fi
