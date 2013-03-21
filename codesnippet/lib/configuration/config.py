# -*- coding: utf-8 -*-

import sys
import os
import os.path

try:
    import yaml
except ImportError as e:
    print(e)
    sys.exit(1)

from .exceptions import ConfigurationException


class Configuration(object):
    def __init__(self, config_filename='', app_name='', cb_check_config=None):
        self._config_filename = config_filename
        self._application_name = app_name
        self._cb_check_config = cb_check_config
        self._config = {}
        self._read_configuration()
        if not self._check_configuration():
            raise ConfigurationException('Configuration has faults')

    def _read_configuration(self):
        if self._config_filename is None or self._config_filename == '':
            raise ValueError('Config Filename is None or Empty')
        fp = open(self._config_filename, 'rb')
        self._config = yaml.load(fp)

    def _check_configuration(self):
        if self._application_name not in self._config:
            raise ValueError('Application Name: {0} not in configuration')
        result = self._cb_check_config(self._config, self._application_name)
        return result

    def _get_config(self):
        return self._config
    config = property(_get_config)