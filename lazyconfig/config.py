# -*- coding: utf-8 -*-

import argparse
import yaml


def lazyfy(value):
    if type(value) == dict:
        value = LazyObject(**value)
    elif type(value) == list:
        value = map(lazyfy, value)
    return value


class LazyObject(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            k = k.replace('-', '_')
            v = lazyfy(v)
            setattr(self, k, v)


class LazyConfigLoader(object):

    def load_dict(self, conf):
        return LazyObject(**conf)

    def load_yaml(self, filename):
        with open(filename, 'r') as f:
            return self.load_dict(yaml.load(f))


def load():
    parser = argparse.ArgumentParser()
    configure_parser(parser)
    args = parser.parse_args()
    cf = LazyConfigLoader()
    return cf.load_yaml(args.config)


def configure_parser(parser):
    parser.add_argument('-c', '--config', help='Yaml configuration file', type=str, default='config.yaml', metavar='<filename>')
