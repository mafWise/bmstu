#!/bin/bash

gcc -o app.o -c main.c -std=gnu99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla --coverage
gcc -o file_funcs.o -c file_funcs.c -std=gnu99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla --coverage
gcc -o student_funcs.o -c student_funcs.c -std=gnu99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla --coverage
gcc -o students_funcs.o -c students_funcs.c -std=gnu99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla --coverage

gcc -o app.exe app.o file_funcs.o student_funcs.o students_funcs.o -lm --coverage
