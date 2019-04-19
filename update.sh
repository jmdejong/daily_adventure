#!/usr/bin/env bash

cd `dirname $0`

python3 -m dailyadventure update>> da.stdout.log 2>>da.stderr.log
