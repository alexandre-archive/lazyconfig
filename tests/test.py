# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.append('./')


class TestLazyConfig(unittest.TestCase):

    def test_custom_filename(self):
        from lazyconfig import LazyConfig

        lc = LazyConfig()
        lc.set_config_file('tests/data/example.yaml')
        lc.load()

        self.assertTrue(lc.loaded)
        self.assertTrue(lc.config is not None)
        self.assertEquals(lc.filename, 'tests/data/example.yaml')

    def test_default_filename(self):
        from lazyconfig import LazyConfig

        lc = LazyConfig()
        lc.load()

        self.assertTrue(lc.loaded)
        self.assertTrue(lc.filename is not None)
        self.assertTrue(lc.filename.endswith('config.yaml'))
        self.assertEquals(lc.config.foo.bar, 'test')

    def test_load_modules_before_setup(self):
        import fileone
        import filetwo
        from lazyconfig import lazyconfig

        lazyconfig.set_config_file('tests/data/name.yaml')

        self.assertEquals(lazyconfig.config.name, 'foobar')
        self.assertEquals(fileone.get_name(), 'foobar')
        self.assertEquals(filetwo.get_name(), 'foobar')

    def test_load_modules_after_setup(self):
        from lazyconfig import lazyconfig

        lazyconfig.set_config_file('tests/data/name.yaml')

        import fileone
        import filetwo

        self.assertEquals(lazyconfig.config.name, 'foobar')
        self.assertEquals(fileone.get_name(), 'foobar')
        self.assertEquals(filetwo.get_name(), 'foobar')


if __name__ == '__main__':
    unittest.main()
