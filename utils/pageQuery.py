# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from requests import HTTPError

def pageQuery(domain):
  """
  通过二次查询获取域名查询详细信息
  :param domain: 查询的域名
  :return: 返回whois查询后的内容
  """
  if domain == None:
    return '你输入的是个啥玩意,别胡闹!!!'
  url = 'http://whois.stupig.com/?domain=' + str(domain)
  try:
    requestsObj = requests.get(url=url)
    requestsObj.raise_for_status()
    requestsObj.encoding = requestsObj.apparent_encoding
    soupHtml = BeautifulSoup(requestsObj.text, 'html.parser')
    return soupHtml.pre.string
  except (HTTPError):
    return '不好意思,稍等一会,服务器去撩妹了!!!'