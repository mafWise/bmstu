#!/bin/bash

gcc -c main.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3
gcc -o main.exe main.o -lm
