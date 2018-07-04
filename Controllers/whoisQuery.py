# -*- coding: utf-8 -*-
import tornado.web
from utils import analysisHtml,pageQuery

class WhoisApiHandler(tornado.web.RequestHandler):
  def get(self):
    query_domain = self.get_argument('domain')
    if query_domain != None or query_domain != '':
      domain_data = analysisHtml.analysisA(query_domain)
    self.write(domain_data)
  def post(self, *args, **kwargs):
    query_domain = self.get_argument('domain')
    if query_domain != None or query_domain != '':
      domain_data = analysisHtml.analysisA(query_domain)
    self.write(domain_data)

class IndexHandler(tornado.web.RequestHandler):
  def get(self):
    query_domain = self.get_argument('domain',default=None)
    page_data_string = ''
    if query_domain != None and query_domain != '':
      domain_data = analysisHtml.analysisA(query_domain)
      domain_name = domain_data.get('域名')
      page_data_string = pageQuery.pageQuery(domain_name)
    self.render('index.html', domain_data=page_data_string)
  def post(self, *args, **kwargs):
    query_domain = self.get_argument('domain')
    page_data_string = ''
    if query_domain != None and query_domain != '':
      domain_data = analysisHtml.analysisA(query_domain)
      domain_name = domain_data.get('域名')
      page_data_string = pageQuery.pageQuery(domain_name)
    self.render('index.html', domain_data = page_data_string)