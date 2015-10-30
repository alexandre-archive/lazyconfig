# -*- coding: utf-8 -*-

import os
import sys
import yaml


def _generate_object(value):
    if type(value) == dict:
        value = ConfigObject(**value)
    elif type(value) == list:
        value = map(_generate_object, value)
    return value


def _generate_dict(o):
    d = {}

    # TODO: Improve this
    for k, v in o.__dict__.items():
        if isinstance(v, ConfigObject):
            d[k] = _generate_dict(v)
        else:
            d[k] = v

    return d


class ConfigObject(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            k = k.replace('-', '_')
            v = _generate_object(v)
            setattr(self, k, v)

    def as_dict(self):
        return _generate_dict(self)


class ConfigLoader(object):

    def load_dict(self, conf):
        return ConfigObject(**conf)

    def load_yaml_file(self, filename):
        with open(filename, 'r') as f:
            return self.load_dict(yaml.load(f))

    def load(self):
        yaml_file = LazyConfig.yaml_file
        if yaml_file is None:
            yaml_file = os.path.join(os.path.dirname(sys.argv[0]), 'config.yaml')
        return self.load_yaml_file(yaml_file)


class LazyConfig(object):
    yaml_file = None

    @classmethod
    def set_config_file(cls, filename):
        cls.yaml_file = filename

    @property
    def config(self):
        self.load()
        return self._config

    def load(self, force_reload=False):
        loaded = getattr(self, 'loaded', False)
        if not loaded:
            self._config = ConfigLoader().load()
            setattr(self, 'loaded', True)
