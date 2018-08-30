#!/usr/bin/env bash
python3 main.py >> /dev/null &
if [[ $? != 0 ]]; then
  python main.py >> /dev/null &
fi