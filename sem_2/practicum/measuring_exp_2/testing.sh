#!/bin/bash

max_size="$2"
min_size="$1"
step="$3"
opts="O1 O2 O3 O0 Os"
counters="1 2"
count="$4"

for co in $(seq "$count"); do
	for opt in $opts; do
		for c in $counters; do
			for ((i = $min_size; i <= $max_size; i=$(( $i + $step )))); do
				echo -n -e "Круг тестирования: $co/$count Файл: 0${c}_${opt}_${i}  \r"
				./apps/app_0"${c}"_"${opt}"_"${i}".exe >> ./data/0"${c}"_"${opt}"_"${i}".txt
			done
		done
	done
done
echo ""
