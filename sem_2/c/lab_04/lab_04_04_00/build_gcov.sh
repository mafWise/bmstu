#!/bin/bash

gcc -o app.o -c main.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 --coverage -Wvla
gcc -o app.exe app.o -lm --coverage
