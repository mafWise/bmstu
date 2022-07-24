#!/bin/bash

file1="$1"
file2="$2"

test_file1=$(grep -E -o "Result: [0-9]+\.[0-9]+" "$file2")
test_file2=$(grep -E -o "Result: [0-9]+\.[0-9]+" "$file1")

if [ "$test_file1" == "$test_file2" ]; then
	exit 0
else
	exit 1
fi
