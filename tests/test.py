# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.append('./')

from lazyconfig import lazyconfig, LazyConfig


class TestLazyConfig(unittest.TestCase):

    def setUp(self):
        LazyConfig.yaml_file = None
        LazyConfig.loaded = False

    def test_custom_filename(self):
        self.assertEquals(LazyConfig.yaml_file, None)
        self.assertFalse(LazyConfig.loaded)
        lazyconfig.set_config_file('tests/data/example.yaml')
        lazyconfig.load()
        self.assertTrue(lazyconfig.config is not None)
        self.assertEquals(LazyConfig.yaml_file, 'tests/data/example.yaml')
        self.assertTrue(LazyConfig.loaded)

    def test_custom_filename_class(self):
        self.assertEquals(LazyConfig.yaml_file, None)
        self.assertFalse(LazyConfig.loaded)
        LazyConfig.set_config_file('tests/data/example.yaml')
        lazyconfig.load()
        self.assertTrue(lazyconfig.config is not None)
        self.assertEquals(LazyConfig.yaml_file, 'tests/data/example.yaml')
        self.assertTrue(LazyConfig.loaded)

    def test_default_filename(self):
        self.assertEquals(lazyconfig.config.foo.bar, 'test')
        self.assertTrue(lazyconfig.yaml_file is not None)
        self.assertTrue(lazyconfig.yaml_file.endswith('config.yaml'))
        self.assertTrue(lazyconfig.loaded)


if __name__ == '__main__':
    unittest.main()
