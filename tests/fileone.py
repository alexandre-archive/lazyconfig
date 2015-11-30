# -*- coding: utf-8 -*-

import sys

sys.path.append('./')

from lazyconfig import lazyconfig


def get_name():
    return lazyconfig.config.name
