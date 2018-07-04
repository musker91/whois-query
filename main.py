# -*- coding: utf-8 -*-

import tornado.ioloop
from tornado.options import define, options
from app_route import RouteSettings

define('port', default=8080, help='server default port', type=int)

if __name__ == '__main__':
  app = RouteSettings().tornadoRoute()
  tornado.options.parse_command_line()
  port = options.port
  app.listen(port)
  tornado.ioloop.IOLoop.instance().start()