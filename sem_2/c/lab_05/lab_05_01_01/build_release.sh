#!/bin/bash

gcc -o app.o -c main.c -std=c99 -Wall -Werror -Wpedantic -Wextra -O2 -Wfloat-equal -Wfloat-conversion -Wvla
gcc -o process.o -c process.c -std=c99 -Wall -Werror -Wpedantic -Wextra -O2 -Wfloat-equal -Wfloat-conversion -Wvla

gcc -o app.exe app.o process.o -lm

