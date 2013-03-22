# -*- coding: utf-8 -*-

import sys

try:
    from .lib.configuration import Configuration
except ImportError as e:
    print('You did not install codesnippets correctly')
    print(('Exception in file {0}: {1}'.format(__file__, e)))
    sys.exit(1)

try:
    from settings import CONFIG_FILE
except ImportError as e:
    print('You don\'t have a settings.py file')
    print(('Exception in file {0}: {1}'.format(__file__, e)))
    sys.exit(1)


def config_check(config=None, app_name=None):
    if config is None:
        return False
    if app_name is None or app_name == '':
        return False
    if app_name not in config:
        return False
    if 'databases' not in config[app_name]:
        return False
    if app_name not in config[app_name]['databases']:
        return False
    if 'host' not in config[app_name]['databases'][app_name]:
        return False
    if 'port' not in config[app_name]['databases'][app_name]:
        return False
    if 'user' not in config[app_name]['databases'][app_name]:
        return False
    if 'pw' not in config[app_name]['databases'][app_name]:
        return False
    return True

def setup_app(config_filename):
    config = Configuration(config_filename, 'codesnippets', config_check)
    return config



configuration = setup_app(CONFIG_FILE)

urls = []
