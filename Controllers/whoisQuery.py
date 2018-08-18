# -*- coding: utf-8 -*-
import tornado.web
from utils.whois_data import WhoisData
from config import *

whois_query = WhoisData(options.cache)


class WhoisApiHandler(tornado.web.RequestHandler):
  def get(self):
    domain_data = {'code': -1}
    query_domain = self.get_argument('domain', None)
    if query_domain:
      domain_data = whois_query.query(query_domain, 'api')
    return self.write(domain_data)

  def post(self, *args, **kwargs):
    self.get()


class IndexHandler(tornado.web.RequestHandler):
  def get(self):
    query_domain = self.get_argument('domain', None)
    page_data_string, domain_name = '', ''
    if query_domain:
      domain_name, page_data_string = whois_query.query(query_domain, 'page')
    self.render('index.html', domain_data=page_data_string, domain=domain_name)

  def post(self, *args, **kwargs):
    self.get()


class PageError(tornado.web.RequestHandler):
  def get(self, *args, **kwargs):
    return self.redirect('/')

  def post(self, *args, **kwargs):
    self.get()
