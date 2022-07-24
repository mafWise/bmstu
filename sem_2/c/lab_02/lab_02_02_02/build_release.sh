#!/bin/bash

gcc -c main.c -std=c99 -Wall -Werror -Wpedantic -Wextra -O2 -Wfloat-equal -Wfloat-conversion -Wvla
gcc -o main.exe main.o -lm
