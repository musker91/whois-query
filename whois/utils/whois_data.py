# -*- coding: utf-8 -*-
import hashlib, threading, time, requests, jdb2
from requests import HTTPError, ConnectionError
from bs4 import BeautifulSoup


class WhoisData:
  def __init__(self, day):
    """
    :param day: 多少天清除一次缓存
    """
    self.nosql_db = jdb2.NoSql(dump=False, nosqlFile='utils/nosql.db', dumpTime=2).createDB('whois')
    t = threading.Thread(target=self.__clear_db_cache, args=(day,))
    t.start()

  def __clear_db_cache(self, day):
    while True:
      _time = 86400
      time.sleep(_time * day)
      print('aaa')
      del self.nosql_db
      self.nosql_db = jdb2.NoSql().createDB('whois')

  def __cn_to_en(self, data):
    """
      将中文转换为英文
      :param data: 源数据
      :return: dict
      """
    if data.get('code') == -1:
      return data
    new_dict = {}
    new_dict['domain'] = data.get('域名')
    new_dict['registrar'] = data.get('注册商')
    new_dict['contacts'] = data.get('联系人')
    new_dict['contactsEmail'] = data.get('联系邮箱')
    new_dict['contactsPhone'] = data.get('联系电话')
    new_dict['creationTime'] = data.get('创建时间')
    new_dict['expiryTime'] = data.get('过期时间')
    new_dict['domainnNameServer'] = data.get('域名服务器')
    new_dict['DNS'] = data.get('DNS')
    new_dict['status'] = data.get('状态')
    new_dict['code'] = data.get('code')
    return new_dict

  def __md5_encrypt(self, string):
    """
     对字符串进行MD5加密
     :param string: 要进行加密的字符串
     :return: 加密后是十六进制字符串
     """
    obj = hashlib.md5()
    obj.update(string.encode('utf-8'))
    encry_string = obj.hexdigest()
    return encry_string

  def __analysisA(self, domain):
    """
    http://whois.chaicp.com/home_whois/cha?ym=domain
    :param domain: 查询的域名
    :return: 返回解析后的json对象
    """
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    url = 'http://whois.chaicp.com/home_whois/cha?ym=' + str(domain)
    data_json = {}
    try:
      requestsObj = requests.get(url=url, headers=headers)
      requestsObj.raise_for_status()
      requestsObj.encoding = requestsObj.apparent_encoding
      data_soup = BeautifulSoup(requestsObj.text, 'html.parser')
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
      data_json = {'code': -1}
    return data_json

  def __whileSelect(self, domain):
    """
    循环查询whois，如果失败再次查询，最多三次
    :param domain: 域名
    :return: 查询后结果，dict/string
    """
    for i in range(3):
      data = self.__analysisA(domain)
      if data.get('code') == 1:
        return data
    return data

  def __pageQuery(self, domain):
    """
    通过二次查询获取域名查询详细信息
    :param domain: 查询的域名
    :return: 返回whois查询后的内容
    """
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    if domain == None:
      return '你输入的是个啥玩意,别胡闹兄嘚!!!'
    url = 'http://da.ai/' + str(domain)
    try:
      requestsObj = requests.get(url=url, headers=headers)
      requestsObj.raise_for_status()
      requestsObj.encoding = requestsObj.apparent_encoding
      soupHtml = BeautifulSoup(requestsObj.text, 'html.parser')
      return soupHtml.pre.string
    except (HTTPError, ConnectionError):
      return '不好意思,稍等一会,服务器去撩妹了!!!'

  def __api(self, domain):
    if domain in self.nosql_db.getKeys():
      _db_domain_data = self.nosql_db.createTable(domain).getValue('api')
      if not _db_domain_data:
        _domain_data = self.__whileSelect(domain)
        domain_data = self.__cn_to_en(_domain_data)
      else:
        domain_data = _db_domain_data
    else:
      _domain_data = self.__whileSelect(domain)
      domain_data = self.__cn_to_en(_domain_data)
    if (domain and domain_data) and domain_data.get('code') == 1:
      self.nosql_db.createTable(domain).setValue('api', domain_data)
    return domain_data

  def __page(self, domain):
    domain_name = self.__api(domain).get('domain', None)
    if domain_name:
      if domain_name in self.nosql_db.getKeys():
        _db_page_data = self.nosql_db.createTable(domain_name).getValue('page')
        if not _db_page_data:
          page_data = self.__pageQuery(domain_name)
        else:
          page_data = _db_page_data
      else:
        page_data = self.__pageQuery(domain_name)
    else:
      page_data = None
    if domain_name and page_data:
      self.nosql_db.createTable(domain_name).setValue('page', page_data)
    else:
      domain_name, page_data = '', '你输入的是个啥玩意,别胡闹兄嘚!!!'
    return domain_name, page_data

  def query(self, domain, tp):
    """
    :param domain: domain name
    :param tp: api,page
    :return:
    """
    if tp == 'page':
      return self.__page(domain)
    elif tp == 'api':
      return self.__api(domain)
