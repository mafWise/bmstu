#!/bin/bash

gcc -o app.o -c main.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla
gcc -o calc_funcs.o -c calc_funcs.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla
gcc -o file_funcs.o -c file_funcs.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla

gcc -o app.exe app.o calc_funcs.o file_funcs.o -lm
