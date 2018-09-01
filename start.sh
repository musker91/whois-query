#!/usr/bin/env bash
WHOIS_DIR=`pwd`/whois-query/main.py
python3 ${WHOIS_DIR} --logging=none
if [[ $? != 0 ]]; then
  python ${WHOIS_DIR} --logging=none
fi
