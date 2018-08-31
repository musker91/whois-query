#!/usr/bin/env bash
_NOW_PATH=`pwd`
python3 ${_NOW_PATH}/main.py --logging=none
if [[ $? != 0 ]]; then
  python ${_NOW_PATH}/main.py --logging=none
fi