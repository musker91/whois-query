# -*- coding: utf-8 -*-
import requests
from requests import HTTPError
from bs4 import BeautifulSoup

def analysisA(domain):
  """
  http://whois.chaicp.com/home_whois/cha?ym=domain
  :param domain: 查询的域名
  :return: 返回解析后的json对象
  """
  headers = {
    'User-Agent': """Mozilla/5.0 (Windows NT 10.0; WOW64) 
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36
    """
    }
  url = 'http://whois.chaicp.com/home_whois/cha?ym=' + str(domain)
  data_json = {}
  try:
    requestsObj = requests.get(url=url, )
    requestsObj.raise_for_status()
    requestsObj.encoding = requestsObj.apparent_encoding
    data_soup = BeautifulSoup(requestsObj.text,'html.parser')
    domain_data_html = data_soup.find_all('ul', attrs={'class': 'whois-list'})[0].children
    for li in domain_data_html:
      if li.name != None:
        li_children = li.children
        key, val = None, None
        for div in li_children:
          if div.name != None:
            attr_dic = div.attrs
            if 'fl' in attr_dic.get('class'):
              key = div.string.split('：')[0]
            elif 'fr' in attr_dic.get('class'):
              val = div.string
        data_json[key] = val
    data_json['code'] = 1
  except (HTTPError, IndexError):
    data_json = {'code': -1, 'msg': '你输入的是个啥玩意,别胡闹!!!'}
  return data_json