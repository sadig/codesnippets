# -*- coding: utf-8 -*-

import sys
import json

try:
    import web
except ImportError as e:
    print('You did not install web.py')
    print(('Exception in file {0}: {1}'.format(__file__, e)))
    sys.exit(1)


try:
    from codesnippet.lib.restify import ResourceView
except ImportError as e:
    print('You did not install web.py')
    print(('Exception in file {0}: {1}'.format(__file__, e)))
    sys.exit(1)

try:
    from codesnippet.globals import urls
except ImportError as e:
    print('You did not install web.py')
    print(('Exception in file {0}: {1}'.format(__file__, e)))
    sys.exit(1)


class SnippetView(ResourceView):

    def GET(self, name=None):
        web.debug(name)
        if name is None or name == '':
            web.debug('{0}: {1}'.format(__file__, self.__class__.__name__))
            data = [
                {'name':'hilfe'},
                {'name':'hier'},
                {'name':'foo'}
            ]
            return self._render(data)

        if name is not None:
            pass

