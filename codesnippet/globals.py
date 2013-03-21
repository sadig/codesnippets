# -*- coding: utf-8 -*-

import sys

try:
    from codesnippets.lib import Configuration
except ImportError as e:
    print('You did not install codesnippets correctly')
    print(('Exception: {0}'.format(e)))
    sys.exit(1)

try:
    from settings import CONFIG_FILE
except ImportError as e:
    print('You don\'t have a settings.py file')
    print(('Exception: {0}'.format(e)))
    sys.exit(1)


def setup_app(config_filename):
    config = Configuration(config_filename)
    return config


configuration = setup_app(CONFIG_FILE)