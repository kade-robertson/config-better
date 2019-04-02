import os
import sys
import unittest

import configbetter

        
class TestMakedirs(unittest.TestCase):
    def setUp(self):
        configbetter.sys.platform = sys.platform
        if sys.platform in ['linux', 'darwin']:
            configbetter.os.environ['HOME'] = os.path.expanduser('~')
        elif sys.platform == 'win32':
            configbetter.os.environ['APPDATA'] = os.environ['APPDATA']
        if 'XDG_DATA_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_DATA_HOME']
        if 'XDG_CONFIG_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_CONFIG_HOME']
        if 'XDG_CACHE_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_CACHE_HOME']
        print(configbetter.os.environ)
        self.conf = configbetter.Config('notarealapp')
        self.conf.makedirs()
   
    def tearDown(self):
        if os.path.exists(self.conf.cache):
            os.rmdir(self.conf.cache)
        if os.path.exists(self.conf.config):
            os.rmdir(self.conf.config)
        if os.path.exists(self.conf.data):
            os.rmdir(self.conf.data)
    
    def test_data_dir(self):
        self.assertTrue(os.path.exists(self.conf.data))
        
    def test_config_dir(self):
        self.assertTrue(os.path.exists(self.conf.config))
        
    def test_cache_dir(self):
        self.assertTrue(os.path.exists(self.conf.cache))


class TestWindowsNoXDG(unittest.TestCase):
    def setUp(self):
        configbetter.sys.platform = 'win32'
        configbetter.os.environ['APPDATA'] = 'C:\\fakedir'
        self.conf = configbetter.Config('fakeapp')

    def test_noxdg_data(self):
        checkdata = os.path.join('C:\\fakedir', 'fakeapp', 'Data')
        self.assertEqual(self.conf.data, checkdata)

    def test_noxdg_config(self):
        checkconfig = os.path.join('C:\\fakedir', 'fakeapp', 'Config')
        self.assertEqual(self.conf.config, checkconfig)

    def test_noxdg_cache(self):
        checkcache = os.path.join('C:\\fakedir', 'fakeapp', 'Cache')
        self.assertEqual(self.conf.cache, checkcache)


class TestLinuxNoXDG(unittest.TestCase):
    def setUp(self):
        configbetter.sys.platform = 'linux'
        configbetter.os.environ['HOME'] = '/fakedir'
        self.conf = configbetter.Config('fakeapp')

    def test_noxdg_data(self):
        checkdata = os.path.join('/fakedir', '.local', 'share', 'fakeapp')
        self.assertEqual(self.conf.data, checkdata)

    def test_noxdg_config(self):
        checkconfig = os.path.join('/fakedir', '.config', 'fakeapp')
        self.assertEqual(self.conf.config, checkconfig)

    def test_noxdg_cache(self):
        checkcache = os.path.join('/fakedir', '.cache', 'fakeapp')
        self.assertEqual(self.conf.cache, checkcache)


class TestMacNoXDG(unittest.TestCase):
    def setUp(self):
        configbetter.sys.platform = 'darwin'
        configbetter.os.environ['HOME'] = '/fakedir'
        self.conf = configbetter.Config('fakeapp')

    def test_noxdg_data(self):
        checkdata = os.path.join('/fakedir', 'Library', 'fakeapp')
        self.assertEqual(self.conf.data, checkdata)

    def test_noxdg_config(self):
        checkconfig = os.path.join('/fakedir', 'Library', 'Preferences', 'fakeapp')
        self.assertEqual(self.conf.config, checkconfig)

    def test_noxdg_cache(self):
        checkcache = os.path.join('/fakedir', 'Library', 'Caches', 'fakeapp')
        self.assertEqual(self.conf.cache, checkcache)


class TestXDG(unittest.TestCase):
    def setUp(self):
        configbetter.sys.platform = 'win32'
        configbetter.os.environ['XDG_DATA_HOME'] = '/xdgdatadir'
        configbetter.os.environ['XDG_CONFIG_HOME'] = '/xdgconfigdir'
        configbetter.os.environ['XDG_CACHE_HOME'] = '/xdgcachedir'
        self.conf = configbetter.Config('fakeapp')

    def test_xdg_data(self):
        checkdata = os.path.join('/xdgdatadir', 'fakeapp')
        self.assertEqual(self.conf.data, checkdata)

    def test_xdg_config(self):
        checkconfig = os.path.join('/xdgconfigdir', 'fakeapp')
        self.assertEqual(self.conf.config, checkconfig)

    def test_xdg_cache(self):
        checkcache = os.path.join('/xdgcachedir', 'fakeapp')
        self.assertEqual(self.conf.cache, checkcache)


if __name__ == '__main__':
    unittest.main()
