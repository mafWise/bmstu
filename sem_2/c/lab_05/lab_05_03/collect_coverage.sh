#!/bin/bash

./build_gcov.sh
cd func_tests/scripts && ./func_tests.sh -q
cd ../..
gcov -r app.exe

