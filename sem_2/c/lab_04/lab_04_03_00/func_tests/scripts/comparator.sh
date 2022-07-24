#!/bin/bash

file1="$1"
file2="$2"

test_file1=$(grep -E -o "([A-Za-z0-9]*\ ?)+" "$file2" | tr -d "\n\t ")
test_file2=$(grep -E -o "([A-Za-z0-9]*\ ?)+" "$file1" | tr -d "\n\t ")

if [ "$test_file1" == "$test_file2" ]; then
	exit 0
fi
exit 1
