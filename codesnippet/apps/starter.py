# -*- coding: utf-8 -*-

import sys


try:
    import web
except ImportError as e:
    print('You didn\'t install web.py')
    print(('Exception: {0}'.format(e)))
    sys.exit(1)


urls = (
    '/.*', 'restapi'
    )
app = web.application(urls, globals())
