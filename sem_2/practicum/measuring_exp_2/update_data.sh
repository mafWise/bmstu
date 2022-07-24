#!/bin/bash

gcc -std=c11 -Wall -Werror -Wpedantic -Wextra -DNMAX="$3" -"$2" main_0"$1".c -o ./apps/app_0"$1"_"$2"_"$3".exe

for i in $(seq "$4"); do
	echo -e -n "Круг тестирования: $i / $4\r"
	./apps/app_0"${1}"_"${2}"_"${3}".exe >> ./data/0"${1}"_"${2}"_"${3}".txt
done
