#!/bin/bash

gcc -o app.o -c main.c -std=c99 -Wall -Werror -Wpedantic -Wextra -O2 -Wfloat-conversion -Wfloat-equal -Wvla
gcc -o process.o -c process.c -std=c99 -Wall -Werror -Wpedantic -Wextra -O2 -Wfloat-conversion -Wfloat-equal -Wvla
gcc -o file_check.o -c file_check.c -std=c99 -Wall -Werror -Wpedantic -Wextra -O2 -Wfloat-conversion -Wfloat-equal -Wvla

gcc -o app.exe app.o process.o file_check.o -lm


