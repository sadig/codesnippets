# -*- coding: utf-8 -*-

import sys


try:
    import web
except ImportError as e:
    print('You didn\'t install web.py')
    print(('Exception in file {0}: {1}'.format(__file__, e)))
    sys.exit(1)


from codesnippet.apps.snippets import SnippetView

urls = [
    '/snippets/(.*)', 'SnippetView'
    ]

app = web.application(urls, globals())
