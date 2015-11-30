# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.append('./..')

from lazyconfig import lazyconfig, LazyConfig


class TestLazyConfig(unittest.TestCase):

    def setUp(self):
        LazyConfig.yaml_file = None
        LazyConfig.loaded = False

    def test_custom_filename(self):
        self.assertIsNone(LazyConfig.yaml_file)
        self.assertFalse(LazyConfig.loaded)
        lazyconfig.set_config_file('data/example.yaml')
        lazyconfig.load()
        self.assertIsNotNone(lazyconfig.config)
        self.assertEquals(LazyConfig.yaml_file, 'data/example.yaml')
        self.assertTrue(LazyConfig.loaded)

    def test_custom_filename_class(self):
        self.assertIsNone(LazyConfig.yaml_file)
        self.assertFalse(LazyConfig.loaded)
        LazyConfig.set_config_file('data/example.yaml')
        lazyconfig.load()
        self.assertIsNotNone(lazyconfig.config)
        self.assertEquals(LazyConfig.yaml_file, 'data/example.yaml')
        self.assertTrue(LazyConfig.loaded)

    def test_default_filename(self):
        self.assertEquals(lazyconfig.config.foo.bar, 'test')
        self.assertIsNotNone(lazyconfig.yaml_file)
        self.assertTrue(lazyconfig.yaml_file.endswith('config.yaml'))
        self.assertTrue(lazyconfig.loaded)


if __name__ == '__main__':
    unittest.main()
