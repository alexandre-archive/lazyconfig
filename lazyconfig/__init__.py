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

    def __init__(self, filename=None):
        self.filename = filename
        self.loaded = False

    @property
    def config(self):
        if not self.loaded:
            self.load()

        return self._config

    @property
    def default_config_file(self):
        return os.path.join(os.path.dirname(sys.argv[0]), 'config.yaml')

    def set_config_file(self, filename):
        if self.filename != filename:
            self.loaded = False
            self.filename = filename

        return self

    def load_from_dict(self, conf):
        self._config = ConfigObject(**conf)
        self.loaded = True
        return self

    def load_from_yaml(self, filename):
        with open(filename, 'r') as f:
            self.load_from_dict(yaml.load(f))

        return self

    def load(self, filename=None):
        if filename:
            file_to_load = filename
        elif self.filename:
            file_to_load = self.filename
        else:
            file_to_load = self.default_config_file

        force_reload = self.filename != file_to_load

        if force_reload or not self.loaded:
            self.filename = file_to_load
            self.load_from_yaml(file_to_load)

        return self

    def reload(self):
        self.loaded = False
        return self.load()

lazyconfig = LazyConfig()
