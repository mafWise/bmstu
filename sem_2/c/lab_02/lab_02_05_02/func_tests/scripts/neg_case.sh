#!/bin/bash

falls_counter=0
app_args=""
test_counter=1

for file in ../data/*; do
	if ! echo "$file" | grep -E -q "neg_.._in"; then
		continue
	fi

	if [ -n "$USE_VALGRIND" ]; then
        	eval valgrind -q ./../../main.exe "$app_args" < "$file" > ../data/tmp_out.txt
	else
		eval ./../../main.exe "$app_args" < "$file" > ../data/tmp_out.txt
	fi

	code1=$?

        if [ "$code1" -ne 0 ]; then
                echo -e "\033[33mTEST$test_counter\033[0m: \033[42mPASS\033[0m"
        else
		falls_counter=$((falls_counter+1))
                echo -e "\033[33mTEST$test_counter\033[0m: \033[41mERROR\033[0m"
		diff "${file/in/out}" ../data/tmp_out.txt
		echo ""
        fi
	test_counter=$((test_counter+1))

done
exit $falls_counter

