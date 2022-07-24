#!/bin/bash

shellcheck ./*sh*
cd func_tests/scripts/ && shellcheck ./*sh*
