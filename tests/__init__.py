import os
import unittest
import configbetter

class TestWindowsNoXDG(unittest.TestCase):

    def setUp(self):
        configbetter.sys.platform = 'win32'
        configbetter.os.environ['APPDATA'] = 'C:\\fakedir'
        self.conf = configbetter.Config('fakeapp')

    def test_noxdg_data(self):
        checkdata = os.path.join('C:\\fakedir', 'fakeapp', 'Data')
        self.assertEqual(self.conf.data.replace('\\', '/'), checkdata.replace('\\', '/'))
    
    def test_noxdg_config(self):
        checkconfig = os.path.join('C:\\fakedir', 'fakeapp', 'Config')
        self.assertEqual(self.conf.config.replace('\\', '/'), checkconfig.replace('\\', '/'))

    def test_noxdg_cache(self):
        checkcache = os.path.join('C:\\fakedir', 'fakeapp', 'Cache') 
        self.assertEqual(self.conf.cache.replace('\\', '/'), checkcache.replace('\\', '/'))

class TestLinuxNoXDG(unittest.TestCase):

    def setUp(self):
        configbetter.sys.platform = 'linux'
        configbetter.os.environ['HOME'] = '/fakedir'
        self.conf = configbetter.Config('fakeapp')

    def test_noxdg_data(self):
        checkdata = os.path.join('/fakedir', '.local', 'share', 'fakeapp')
        self.assertEqual(self.conf.data.replace('\\', '/'), checkdata.replace('\\', '/'))
    
    def test_noxdg_config(self):
        checkconfig = os.path.join('/fakedir', '.config', 'fakeapp')
        self.assertEqual(self.conf.config.replace('\\', '/'), checkconfig.replace('\\', '/'))

    def test_noxdg_cache(self):
        checkcache = os.path.join('/fakedir', '.cache', 'fakeapp') 
        self.assertEqual(self.conf.cache.replace('\\', '/'), checkcache.replace('\\', '/'))

class TestMacNoXDG(unittest.TestCase):

    def setUp(self):
        configbetter.sys.platform = 'darwin'
        configbetter.os.environ['HOME'] = '/fakedir'
        self.conf = configbetter.Config('fakeapp')

    def test_noxdg_data(self):
        checkdata = os.path.join('/fakedir', 'Library', 'fakeapp')
        self.assertEqual(self.conf.data.replace('\\', '/'), checkdata.replace('\\', '/'))
    
    def test_noxdg_config(self):
        checkconfig = os.path.join('/fakedir', 'Library', 'Preferences', 'fakeapp')
        self.assertEqual(self.conf.config.replace('\\', '/'), checkconfig.replace('\\', '/'))

    def test_noxdg_cache(self):
        checkcache = os.path.join('/fakedir', 'Library', 'Caches', 'fakeapp')
        self.assertEqual(self.conf.cache.replace('\\', '/'), checkcache.replace('\\', '/'))

class TestXDG(unittest.TestCase):

    def setUp(self):
        configbetter.sys.platform = 'win32'
        configbetter.os.environ['XDG_DATA_HOME'] = '/xdgdatadir'
        configbetter.os.environ['XDG_CONFIG_HOME'] = '/xdgconfigdir'
        configbetter.os.environ['XDG_CACHE_HOME'] = '/xdgcachedir'
        self.conf = configbetter.Config('fakeapp')

    def test_xdg_data(self):
        checkdata = os.path.join('/xdgdatadir', 'fakeapp')
        self.assertEqual(self.conf.data.replace('\\', '/'), checkdata.replace('\\', '/'))
    
    def test_xdg_config(self):
        checkconfig = os.path.join('/xdgconfigdir', 'fakeapp')
        self.assertEqual(self.conf.config.replace('\\', '/'), checkconfig.replace('\\', '/'))

    def test_xdg_cache(self):
        checkcache = os.path.join('/xdgcachedir', 'fakeapp') 
        self.assertEqual(self.conf.cache.replace('\\', '/'), checkcache.replace('\\', '/'))

if __name__ == '__main__':
    unittest.main()