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

    def test_data_dir(cls):
        cls.assertTrue(os.path.exists(cls.conf.data))

    def test_config_dir(cls):
        cls.assertTrue(os.path.exists(cls.conf.config))

    def test_cache_dir(cls):
        cls.assertTrue(os.path.exists(cls.conf.cache))


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

    def test_noxdg_data(cls):
        checkdata = os.path.join(cls.tempdir, 'fakeapp', 'Data')
        cls.assertEqual(cls.conf.data, checkdata)

    def test_noxdg_config(cls):
        checkconfig = os.path.join(cls.tempdir, 'fakeapp', 'Config')
        cls.assertEqual(cls.conf.config, checkconfig)

    def test_noxdg_cache(cls):
        checkcache = os.path.join(cls.tempdir, 'fakeapp', 'Cache')
        cls.assertEqual(cls.conf.cache, checkcache)


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

    def test_noxdg_data(cls):
        checkdata = os.path.join(cls.tempdir, '.local', 'share', 'fakeapp')
        cls.assertEqual(cls.conf.data, checkdata)

    def test_noxdg_config(cls):
        checkconfig = os.path.join(cls.tempdir, '.config', 'fakeapp')
        cls.assertEqual(cls.conf.config, checkconfig)

    def test_noxdg_cache(cls):
        checkcache = os.path.join(cls.tempdir, '.cache', 'fakeapp')
        cls.assertEqual(cls.conf.cache, checkcache)


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

    def test_noxdg_data(cls):
        checkdata = os.path.join(cls.tempdir, 'Library', 'fakeapp')
        cls.assertEqual(cls.conf.data, checkdata)

    def test_noxdg_config(cls):
        checkconfig = os.path.join(cls.tempdir, 'Library', 'Preferences', 'fakeapp')
        cls.assertEqual(cls.conf.config, checkconfig)

    def test_noxdg_cache(cls):
        checkcache = os.path.join(cls.tempdir, 'Library', 'Caches', 'fakeapp')
        cls.assertEqual(cls.conf.cache, checkcache)


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

    def test_xdg_data(cls):
        checkdata = os.path.join(cls.datatempdir, 'fakeapp')
        cls.assertEqual(cls.conf.data, checkdata)

    def test_xdg_config(cls):
        checkconfig = os.path.join(cls.configtempdir, 'fakeapp')
        cls.assertEqual(cls.conf.config, checkconfig)

    def test_xdg_cache(cls):
        checkcache = os.path.join(cls.cachetempdir, 'fakeapp')
        cls.assertEqual(cls.conf.cache, checkcache)


if __name__ == '__main__':
    unittest.main()
