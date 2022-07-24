#!/bin/bash

max_size="$2"
min_size="$1"
step="$3"
opts="Os O0 O1 O2 O3"
all=$(( $(( $(($max_size - $min_size)) / $step + 1)) * 10))
counter=1
for number in 1 2; do
	for opt in $opts; do
		for ((i = $min_size; i <= $max_size; i=$(( $i + $step )))); do
			echo -n -e "Создание приложения [$counter / $all]\r"
			gcc -std=c99 -Wall -Werror -Wpedantic -Wextra \
			-DNMAX="${i}" \
			-"${opt}" \
			main_0"${number}".c -o ./apps/app_0"${number}"_"${opt}"_"${i}".exe
			counter=$(($counter + 1))
		done
	done
done
echo ""
