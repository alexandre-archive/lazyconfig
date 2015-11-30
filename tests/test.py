# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.append('./')

from lazyconfig import LazyConfig


class TestLazyConfig(unittest.TestCase):

    def test_custom_filename(self):
        lc = LazyConfig()
        lc.set_config_file('tests/data/example.yaml')
        lc.load()

        self.assertTrue(lc.loaded)
        self.assertTrue(lc.config is not None)
        self.assertEquals(lc.filename, 'tests/data/example.yaml')

    def test_default_filename(self):
        lc = LazyConfig()
        lc.load()

        self.assertTrue(lc.loaded)
        self.assertTrue(lc.filename is not None)
        self.assertTrue(lc.filename.endswith('config.yaml'))
        self.assertEquals(lc.config.foo.bar, 'test')


if __name__ == '__main__':
    unittest.main()
