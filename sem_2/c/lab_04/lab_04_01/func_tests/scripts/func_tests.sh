#!/bin/bash

if ! [ -e ../../app.exe ]; then
	decision=""
	echo -e "\033[41m\nИсполняемый файл не найден\033[0m\n"
	echo "Собрать отладочный проект?(Yes/no): "; read -r decision
	if [ "$decision" == "Yes" ] || [ "$decision" == "" ]; then
		cd ../../ && ./build_debug.sh
		cd func_tests/scripts/ || exit 1
	else
		exit 1
	fi
fi

mode=""
app_args="$2"

if [ "$1" == "-q" ]; then
	mode="1>/dev/null"
fi

echo -e "\n\033[4mЗАПУСК ПОЗИТИВНЫХ ТЕСТОВ\033[0m\n"

test_counter=1
falls_counter=0
for file in ../data/*; do
        if ! echo "$file" | grep -E -q "pos_.._in"; then
               	continue
       	fi
	./pos_case.sh "$file" "$app_args" "$mode"
	exit_code="$?"

        if [ "$exit_code" -eq 0 ]; then
       	        echo -e "\033[33mTEST$test_counter\033[0m: \033[42mPASS\033[0m"
       	else
               	falls_counter=$((falls_counter+1))
               	echo -e "\033[33mTEST$test_counter\033[0m: \033[41mERROR\033[0m"
               	diff "${file/in/out}" ../data/tmp_out.txt
               	echo ""
       	fi
       	test_counter=$((test_counter+1))
done
echo -e "\nНе пройдено тестов: $falls_counter\n"

rm ../data/tmp_out.txt
