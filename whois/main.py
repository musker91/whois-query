# -*- coding: utf-8 -*-
import logging
import tornado.ioloop
from whois.config import *
from tornado.httpserver import HTTPServer
from whois.app_route import RouteSettings

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
  logging.info("\033[32mListening start -> {addr}:{port}\033[0m".format(**fb))
  tornado.ioloop.IOLoop.current().start()
