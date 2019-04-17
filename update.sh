#!/bin/env bash

cd `dirname $0`

python -m dailyadventure >> da.stdout.log 2>>da.stderr.log
