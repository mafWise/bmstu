#!/bin/bash

echo -e "\n\033[4mЗАПУСК СКРИПТА\033[0m\n"
echo -n "Введите минимальное количество строк (etc -> 50): "
read -r MIN_SIZE

if ! echo "$MIN_SIZE" | grep -Eq "^[0-9]*$" ; then
	echo -e "\033[41mОШИБКА ВВОДА\033[0m"
	exit 1
fi


echo -e -n "Введите максимальное количество строк (etc -> 3000): "
read -r MAX_SIZE

if ! echo "$MAX_SIZE" | grep -Eq "^[0-9]*$" ; then
        echo -e "\033[41mОШИБКА ВВОДА\033[0m"
        exit 1
fi

if [ $((${MAX_SIZE} - ${MIN_SIZE})) -gt 3000 ]; then
	echo -e "\nПри введенных данных программа может серьезно замедлить работоспособность вашей машины"
	echo -n "Продолжить? (yes/No): "; read -r ans
	if [[ "$ans" == "" || "$ans" == "No" ]]; then
		exit 1
	fi
fi

echo -n -e "Введите шаг измерений (etc -> 50): "
read -r STEP

if ! echo "$STEP" | grep -Eq "^[0-9]*$" ; then
        echo -e "\033[41mОШИБКА ВВОДА\033[0m"
        exit 1
fi

if [ "$STEP" -lt 50 ]; then
        echo -e "\nПри введенных данных программа может серьезно замедлить работоспособность вашей машины"
        echo -n "Продолжить? (yes/No): "; read -r ans
        if [[ "$ans" == "" || "$ans" == "No" ]]; then
                exit 1
        fi
fi

echo -n -e "Введите количество кругов тестирования (etc -> 15): "
read -r LAPS

if ! echo "$LAPS" | grep -Eq "^[0-9]*$" ; then
        echo -e "\033[41mОШИБКА ВВОДА\033[0m"
        exit 1
fi

if [ "$LAPS" -gt 15 ]; then
        echo -e "\nПри введенных данных программа может серьезно замедлить работоспособность вашей машины"
        echo -n "Продолжить? (yes/No): "; read -r ans
        if [[ "$ans" == "" || "$ans" == "No" ]]; then
                exit 1
        fi
fi

mkdir ./apps 2>/dev/null
./build_apps.sh "$MIN_SIZE" "$MAX_SIZE" "$STEP"
mkdir ./data 2>/dev/null
./testing.sh "$MIN_SIZE" "$MAX_SIZE" "$STEP" "$LAPS"
mkdir ./preproc 2>/dev/null
python3 make_preproc.py "$MIN_SIZE" "$MAX_SIZE" "$STEP"
mkdir ./graphs 2>/dev/null
python3 make_postproc.py "$MIN_SIZE" "$MAX_SIZE" "$STEP"

