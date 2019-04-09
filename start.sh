#!/usr/bin/env bash
ROOT_DIR="/opt"
WHOIS_MAIN=${ROOT_DIR}/whois-query/main.py
python3 ${WHOIS_MAIN}
if [[ $? != 0 ]]; then
  python ${WHOIS_MAIN}
fi