# -*- coding: utf-8 -*-

import sys
import json

try:
    import web
except ImportError as e:
    print('You did not install web.py')
    print(('Exception in file {0}: {1}'.format(__file__, e)))
    sys.exit(1)


class ResourceView(object):

    def __init__(self):
        pass

    def GET(self, name=None):
        pass

    def POST(self, name=None):
        pass

    def PUT(self, name=None):
        pass

    def DELETE(self, name=None):
        pass

    def _render(self, data=None):
        web.header('Content-Type', 'application/json; charset=utf8')
        return json.dumps(data)