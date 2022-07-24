#!/bin/bash

app_args="$2"
file="$1"

if [ -n "$USE_VALGRIND" ]; then
        eval valgrind -q ./../../app.exe "$app_args" < "$file" > ../data/tmp_out.txt
else
	eval ./../../app.exe "$data" < "$file" > ../data/tmp_out.txt
fi

exit $?

