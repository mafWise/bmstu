#!/bin/bash
if [ "$1" == "-q" ]; then
	./pos_case.sh 1>/dev/null
	code1=$?
	./neg_case.sh 1>/dev/null
	code2=$?
else
	echo -e "\n\033[4mЗАПУСК ПОЗИТИВНЫХ ТЕСТОВ\033[0m\n"
	./pos_case.sh
	code1=$?
	echo -e "\nНепройдено тестов: $?\n"
	echo -e "\n\033[4mЗАПУСК НЕГАТИВНЫХ ТЕСТОВ\033[0m\n"
	./neg_case.sh
        code2=$?
	echo -e "\nНепройдено тестов: $?\n"
fi

if [ "$code1" -ne "0" ] && [ "$code2" -ne "0" ]; then
	exit 1
else
	exit 0
fi
