# -*- coding: utf-8 -*-

import tornado.web
from Controllers import whoisQuery
import os

class RouteSettings(object):
  """
  Tornado 路由类
  def tornadoRoute(self):
    路由主函数
  """
  def __init__(self):
    pass

  def __webDemo(self):
    """
    定义webdemo的路由映射
    :return:webdemo list
    """
    web_demo = [
      (r'/', whoisQuery.IndexHandler),
      (r'/whoisapi/?', whoisQuery.WhoisApiHandler),
      (r".*", whoisQuery.PageError)
    ]
    return web_demo

  def __tempaltePath(self):
    """
    :return: 模板文件路径
    """
    tempalte = os.path.join(os.path.dirname(__file__), 'templates')
    return tempalte

  def __static(self):
    """
    :return: 静态文件路径
    """
    static = os.path.join(os.path.dirname(__file__), 'static')
    return static

  def tornadoRoute(self):
    """
    :return: 返回生成的APP对象
    """
    totle_route = self.__webDemo()
    app = tornado.web.Application(totle_route,
                                  template_path=self.__tempaltePath(),
                                  static = self.__static(),
                                  )
    return app
