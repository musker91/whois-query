# -*- coding: utf-8 -*-

import tornado.ioloop
from tornado.options import define, options
from tornado.httpserver import HTTPServer
from app_route import RouteSettings

define('port', default=8080, help='server default port', type=int)

if __name__ == '__main__':
  app = RouteSettings().tornadoRoute()
  tornado.options.parse_command_line()
  httpserver = HTTPServer(app)
  port = options.port
  # app.listen(port)
  httpserver.bind(port)
  httpserver.start()
  tornado.ioloop.IOLoop.current().start()