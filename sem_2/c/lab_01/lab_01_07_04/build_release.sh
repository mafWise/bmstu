#!/bin/bash

gcc -c main.c -std=c99 -Wall -Werror -Wpedantic -Wextra -lm -Wfloat-equal -Wfloat-conversion
gcc -o main.exe main.o -lm
