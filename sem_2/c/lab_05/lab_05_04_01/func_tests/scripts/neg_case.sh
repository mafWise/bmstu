#!/bin/bash

app_args="$2"
file="$1"
cp "$file" ../data/tmp_out.bin

if [ -n "$USE_VALGRIND" ]; then
        eval valgrind -q ./../../app.exe "$app_args"
else
        eval ./../../app.exe "$app_args"
fi

exit $?
