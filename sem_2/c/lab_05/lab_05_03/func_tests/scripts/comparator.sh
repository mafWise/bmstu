#!/bin/bash

file1="$1"
file2="$2"

if [ -z $(diff "$file1" "$file2") ]; then
	exit 0
fi
exit 1
