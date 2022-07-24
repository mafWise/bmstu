#!/bin/bash

gcc -o app.o -c main.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla
gcc -o digs_funcs.o -c digs_funcs.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla
gcc -o file_funcs.o -c file_funcs.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla
gcc -o get_put_funcs.o -c get_put_funcs.c -std=c99 -Wall -Werror -Wpedantic -Wextra -ggdb -O0 -Wfloat-conversion -Wfloat-equal -g3 -Wvla


gcc -o app.exe app.o digs_funcs.o file_funcs.o get_put_funcs.o -lm
