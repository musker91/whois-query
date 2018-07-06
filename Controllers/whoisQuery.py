# -*- coding: utf-8 -*-
import tornado.web
from utils import pageQuery,cnToEn,whileSelect

class WhoisApiHandler(tornado.web.RequestHandler):
  def get(self):
    query_domain = self.get_argument('domain')
    if query_domain != None or query_domain != '':
      domain_data = cnToEn.cnToEN(whileSelect.whileSelect(query_domain))
    self.write(domain_data)
  def post(self, *args, **kwargs):
    self.get()

class IndexHandler(tornado.web.RequestHandler):
  def get(self):
    query_domain = self.get_argument('domain',default=None)
    page_data_string, domain_name = '', ''
    if query_domain != None and query_domain != '':
      domain_data = cnToEn.cnToEN(whileSelect.whileSelect(query_domain))
      domain_name = domain_data.get('domain')
      page_data_string = pageQuery.pageQuery(domain_name)
      if page_data_string == None or page_data_string == '':
        page_data_string = """
        此域名暂时只能返回这这内容
        """
        for i in domain_data:
          page_data_string += "{}:{}\n".format(i,domain_data.get(i))
    self.render('index.html', domain_data=page_data_string, domain=domain_name)
  def post(self, *args, **kwargs):
    self.get()