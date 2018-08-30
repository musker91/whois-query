#!/usr/bin/env bash
nohup python3 main.py --logging=info >> /dev/null &
if [[ $? != 0 ]]; then
  nohup python main.py --logging=info >> /dev/null &
fi