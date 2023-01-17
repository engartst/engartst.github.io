#!/bin/bash

day=$(date "+%Y%m%d_%H%M%S")
python3 main.py $day
cd log
./makePDF.sh ${day}.md
