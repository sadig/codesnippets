# -*- coding: utf-8 -*-

import sys

try:
    from codesnippets.lib import Configuration
except ImportError as e:
    print('You did not install codesnippets correctly')
    print(('Exception in file {0}: {1}'.format(__file__, e)))
    sys.exit(1)


def setup_app(config_filename):
    config = Configuration(config_filename)
    return config
