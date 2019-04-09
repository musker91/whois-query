# -*- coding: utf-8 -*-
# File: whois.py
# Author: Musker
# Description: Whois server main

import logging
import os
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from whois.apps import views

define('port', default=8080, help='server default port', type=int)
define('cache', default=3, help='domain info cache day', type=int)


class RouteSettings(object):
	"""
	Tornado 路由类
	def tornadoRoute(self):
	  路由主函数
	"""

	def __webDemo(self):
		"""
		定义webdemo的路由映射
		:return:webdemo list
		"""
		web_demo = [
			(r"/", views.IndexHandler),
			(r"/query/?", views.QueryHandler),
			(r"/whoisapi/?", views.WhoisApiHandler),
			(r".*", views.PageError)
		]
		return web_demo

	def __tempaltePath(self):
		"""
		:return: 模板文件路径
		"""
		tempalte = os.path.join(os.path.dirname(__file__), "whois", "templates")
		return tempalte

	def tornadoRoute(self):
		"""
		:return: 返回生成的APP对象
		"""
		totle_route = self.__webDemo()
		return tornado.web.Application(totle_route, template_path=self.__tempaltePath())


def main():
	app = RouteSettings().tornadoRoute()
	tornado.options.parse_command_line()
	httpserver = HTTPServer(app)
	port = options.port
	httpserver.bind(port)
	httpserver.start()
	fb = {
		'addr': '0.0.0.0',
		'port': port
	}
	logging.info("Listening start -> {addr}:{port}".format(**fb))
	tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	main()
