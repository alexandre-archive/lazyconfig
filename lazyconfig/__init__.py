# -*- coding: utf-8 -*-

import sys

from config import LazyConfig

sys.modules[__name__] = LazyConfig()
