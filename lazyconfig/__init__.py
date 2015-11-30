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


def _prop_name(value):
    return value.replace('-', '_')


class ConfigObject(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, _prop_name(k), _generate_object(v))

    def as_dict(self):
        return _generate_dict(self)


class LazyConfig(object):
    yaml_file = None
    loaded = False

    @classmethod
    def set_config_file(cls, filename):
        if cls.yaml_file != filename:
            cls.loaded = False

        cls.yaml_file = filename

    @property
    def config(self):
        if not LazyConfig.loaded:
            self.load()

        return self._config

    def load_dict(self, conf):
        self._config = ConfigObject(**conf)
        LazyConfig.loaded = True
        return self

    def _load_yaml_file(self, filename):
        with open(filename, 'r') as f:
            self.load_dict(yaml.load(f))

    def load(self, filename=None):
        if filename:
            file_to_load = filename
        elif LazyConfig.yaml_file:
            file_to_load = LazyConfig.yaml_file
        else:
            file_to_load = os.path.join(os.path.dirname(sys.argv[0]), 'config.yaml')

        force_reload = LazyConfig.yaml_file != file_to_load

        if force_reload or not LazyConfig.loaded:
            LazyConfig.yaml_file = file_to_load
            self._load_yaml_file(file_to_load)

        return self

    def reload(self):
        LazyConfig.loaded = False
        return self.load()

lazyconfig = LazyConfig()
