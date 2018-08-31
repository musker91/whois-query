#!/usr/bin/env bash
_NOW_PATH=`pwd`
python3 ${_NOW_PATH}/main.py --logging=none  &> /dev/null &
if [[ $? != 0 ]]; then
  python ${_NOW_PATH}/main.py --logging=none &> /dev/null &
fi