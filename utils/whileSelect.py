# -*- coding: utf-8 -*-

from utils import analysisHtml

def whileSelect(domain):
  """
  循环查询whois，如果失败再次查询，最多三次
  :param domain: 域名
  :return: 查询后结果，dict/string
  """
  for i in range(3):
    data = analysisHtml.analysisA(domain)
    if data.get('code') == 1:
      return data
  return data