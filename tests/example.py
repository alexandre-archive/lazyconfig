# -*- coding: utf-8 -*-

import sys
sys.path.append('./..')
import lazyconfig

# lazyconfig.set_config_file('test.yaml')


def print_foo_bar():
    print(lazyconfig.config.foo.bar)

if __name__ == '__main__':
    print_foo_bar()
