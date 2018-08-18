# -*- coding: utf-8 -*-
from tornado.options import define, options

define('port', default=8080, help='server default port', type=int)
define('cache', default=3, help='domain info cache day', type=int)
