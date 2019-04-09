# -*- coding: utf-8 -*-
# File: views.py
# Author: Musker
# Description: App controller

import logging
import time
import tornado.web
import tornado.gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from whois.utils import whoisUtils

now_time = lambda: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


class IndexHandler(tornado.web.RequestHandler):
	"""
	首页
	"""
	executor = ThreadPoolExecutor(15)  # 进程池

	@tornado.gen.coroutine
	def get(self):
		self.render("index.html")
		self.flush()

	@tornado.gen.coroutine
	def post(self, *args, **kwargs):
		self.get()


class WhoisApiHandler(tornado.web.RequestHandler):
	"""
	Http Api 查询
	"""
	executor = ThreadPoolExecutor(15)  # 进程池

	@run_on_executor
	def get_domain_data(self, domain_name):
		return_data = {
			"code": -3,
			"data": None
		}
		# 域名输入有误
		if not domain_name:
			return_data["code"] = "-2"
			return return_data
		try:
			# 开始查询信息
			status, code, data = whoisUtils.getDoaminWhois(domain_name, "d")
			# 状态错误
			if not status:
				return_data["code"] = code
				return return_data
			# 返回正确信息
			return_data["code"], return_data["data"] = code, data
		except Exception as e:
			logging.error("[%s]: %s" % (now_time(), e))
			return_data["code"] = "-4"
		return return_data

	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def get(self):
		domain_name = self.get_argument("domain_name", None)
		return_data = yield self.get_domain_data(domain_name)
		self.write(return_data)

	@tornado.gen.coroutine
	def post(self, *args, **kwargs):
		self.get()

class QueryHandler(tornado.web.RequestHandler):
	"""
	页面ajax查询
	"""
	executor = ThreadPoolExecutor(15)  # 进程池

	@run_on_executor
	def get_domain_data(self, domain_name):
		return_data = {
			"code": -3,
			"data": None
		}
		# 域名输入有误
		if not domain_name:
			return_data["code"] = "-2"
			return return_data
		try:
			# 开始查询信息
			status, code, data = whoisUtils.getDoaminWhois(domain_name, "s")
			# 状态错误
			if not status:
				return_data["code"] = code
				return return_data
			# 返回正确信息
			return_data["code"], return_data["data"] = code, data
		except Exception as e:
			logging.error("[%s]: %s" % (now_time(), e))
			return_data["code"] = "-4"
		return return_data

	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def get(self):
		return_data = {
			"code": -3,
			"data": None
		}
		domain_name = self.get_argument("domain_name", None)
		return_data = yield self.get_domain_data(domain_name)
		self.write(return_data)
		
	@tornado.gen.coroutine
	def post(self, *args, **kwargs):
		self.get()

class PageError(tornado.web.RequestHandler):
	"""
	错误页面
	"""

	def get(self, *args, **kwargs):
		return self.redirect('/')

	def post(self, *args, **kwargs):
		self.get()
