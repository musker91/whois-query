#!/usr/bin/env bash
nohup python main.py --logging=info >> log/whois.log &
if [[ $? != 0 ]]; then
  nohup python3 main.py --logging=info >> log/whois.log &
fi