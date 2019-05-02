import os
import shutil
import sys
import tempfile
import unittest

import configbetter


class TestMakedirs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configbetter.sys.platform = sys.platform
        cls.tempdir = tempfile.mkdtemp()
        if sys.platform in ['linux', 'darwin']:
            configbetter.os.environ['HOME'] = cls.tempdir
        elif sys.platform == 'win32':
            configbetter.os.environ['APPDATA'] = cls.tempdir
        if 'XDG_DATA_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_DATA_HOME']
        if 'XDG_CONFIG_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_CONFIG_HOME']
        if 'XDG_CACHE_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_CACHE_HOME']
        cls.conf = configbetter.Config('notarealapp')
        cls.conf.makedirs()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tempdir)

    def test_data_dir(self):
        self.assertTrue(os.path.exists(self.conf.data))

    def test_config_dir(self):
        self.assertTrue(os.path.exists(self.conf.config))

    def test_cache_dir(self):
        self.assertTrue(os.path.exists(self.conf.cache))

class TestRmdirs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configbetter.sys.platform = 'win32'
        cls.tempdir = tempfile.mkdtemp()
        if sys.platform in ['linux', 'darwin']:
            configbetter.os.environ['HOME'] = cls.tempdir
        elif sys.platform == 'win32':
            configbetter.os.environ['APPDATA'] = cls.tempdir
        if 'XDG_DATA_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_DATA_HOME']
        if 'XDG_CONFIG_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_CONFIG_HOME']
        if 'XDG_CACHE_HOME' in configbetter.os.environ:
            del configbetter.os.environ['XDG_CACHE_HOME']
        cls.conf = configbetter.Config('notarealapp')
        cls.conf.makedirs()
        cls.conf.rmdirs()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tempdir)

    def test_data_rmdir(self):
        self.assertFalse(os.path.exists(self.conf.data))

    def test_config_rmdir(self):
        self.assertFalse(os.path.exists(self.conf.config))

    def test_cache_rmdir(self):
        self.assertFalse(os.path.exists(self.conf.cache))

    def test_windows_edgecase_rmdir(self):
        self.assertFalse(os.path.exists(os.path.join(self.tempdir, 'notarealapp')))


class TestWindowsNoXDG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configbetter.sys.platform = 'win32'
        cls.tempdir = tempfile.mkdtemp()
        configbetter.os.environ['APPDATA'] = cls.tempdir
        cls.conf = configbetter.Config('fakeapp')

    @classmethod
    def tearDownClass(cls):
        os.rmdir(cls.tempdir)

    def test_noxdg_data(self):
        checkdata = os.path.join(self.tempdir, 'fakeapp', 'Data')
        self.assertEqual(self.conf.data, checkdata)

    def test_noxdg_config(self):
        checkconfig = os.path.join(self.tempdir, 'fakeapp', 'Config')
        self.assertEqual(self.conf.config, checkconfig)

    def test_noxdg_cache(self):
        checkcache = os.path.join(self.tempdir, 'fakeapp', 'Cache')
        self.assertEqual(self.conf.cache, checkcache)


class TestLinuxNoXDG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configbetter.sys.platform = 'linux'
        cls.tempdir = tempfile.mkdtemp()
        configbetter.os.environ['HOME'] = cls.tempdir
        cls.conf = configbetter.Config('fakeapp')

    @classmethod
    def tearDownClass(cls):
        os.rmdir(cls.tempdir)

    def test_noxdg_data(self):
        checkdata = os.path.join(self.tempdir, '.local', 'share', 'fakeapp')
        self.assertEqual(self.conf.data, checkdata)

    def test_noxdg_config(self):
        checkconfig = os.path.join(self.tempdir, '.config', 'fakeapp')
        self.assertEqual(self.conf.config, checkconfig)

    def test_noxdg_cache(self):
        checkcache = os.path.join(self.tempdir, '.cache', 'fakeapp')
        self.assertEqual(self.conf.cache, checkcache)


class TestMacNoXDG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configbetter.sys.platform = 'darwin'
        cls.tempdir = tempfile.mkdtemp()
        configbetter.os.environ['HOME'] = cls.tempdir
        cls.conf = configbetter.Config('fakeapp')

    @classmethod
    def tearDownClass(cls):
        os.rmdir(cls.tempdir)

    def test_noxdg_data(self):
        checkdata = os.path.join(self.tempdir, 'Library', 'fakeapp')
        self.assertEqual(self.conf.data, checkdata)

    def test_noxdg_config(self):
        checkconfig = os.path.join(self.tempdir, 'Library', 'Preferences', 'fakeapp')
        self.assertEqual(self.conf.config, checkconfig)

    def test_noxdg_cache(self):
        checkcache = os.path.join(self.tempdir, 'Library', 'Caches', 'fakeapp')
        self.assertEqual(self.conf.cache, checkcache)
        
class TestMacForceUnix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configbetter.sys.platform = 'darwin'
        cls.tempdir = tempfile.mkdtemp()
        configbetter.os.environ['HOME'] = cls.tempdir
        cls.conf = configbetter.Config('fakeapp', force_unix = True)

    @classmethod
    def tearDownClass(cls):
        os.rmdir(cls.tempdir)

    def test_noxdg_data(self):
        checkdata = os.path.join(self.tempdir, '.local', 'share', 'fakeapp')
        self.assertEqual(self.conf.data, checkdata)

    def test_noxdg_config(self):
        checkconfig = os.path.join(self.tempdir, '.config', 'fakeapp')
        self.assertEqual(self.conf.config, checkconfig)

    def test_noxdg_cache(self):
        checkcache = os.path.join(self.tempdir, '.cache', 'fakeapp')
        self.assertEqual(self.conf.cache, checkcache)


class TestXDG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        configbetter.sys.platform = 'win32'
        cls.datatempdir = tempfile.mkdtemp()
        cls.configtempdir = tempfile.mkdtemp()
        cls.cachetempdir = tempfile.mkdtemp()
        configbetter.os.environ['XDG_DATA_HOME'] = cls.datatempdir
        configbetter.os.environ['XDG_CONFIG_HOME'] = cls.configtempdir
        configbetter.os.environ['XDG_CACHE_HOME'] = cls.cachetempdir
        cls.conf = configbetter.Config('fakeapp')

    @classmethod
    def tearDownClass(cls):
        os.rmdir(cls.datatempdir)
        os.rmdir(cls.configtempdir)
        os.rmdir(cls.cachetempdir)

    def test_xdg_data(self):
        checkdata = os.path.join(self.datatempdir, 'fakeapp')
        self.assertEqual(self.conf.data, checkdata)

    def test_xdg_config(self):
        checkconfig = os.path.join(self.configtempdir, 'fakeapp')
        self.assertEqual(self.conf.config, checkconfig)

    def test_xdg_cache(self):
        checkcache = os.path.join(self.cachetempdir, 'fakeapp')
        self.assertEqual(self.conf.cache, checkcache)


if __name__ == '__main__':
    unittest.main()
