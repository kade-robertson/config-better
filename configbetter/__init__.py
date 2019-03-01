import os
import sys


class Config:
    def __init__(self, appname):
        self.appname = appname
        self.__data = None
        self.__config = None
        self.__cache = None
        if 'XDG_DATA_HOME' in os.environ:
            self.__data = os.environ['XDG_DATA_HOME']
        if 'XDG_CONFIG_HOME' in os.environ:
            self.__config = os.environ['XDG_CONFIG_HOME']
        if 'XDG_CACHE_HOME' in os.environ:
            self.__cache = os.environ['XDG_CACHE_HOME']

    def _getdir(self, *pathparts):
        return os.path.expandvars(os.path.join(*pathparts))

    @property
    def data(self):
        if self.__data:
            return self._getdir(self.__data, self.appname)
        elif sys.platform == 'win32':
            return self._getdir(os.environ['APPDATA'], self.appname, 'Data')
        elif sys.platform == 'darwin':
            return self._getdir('$HOME', 'Library', self.appname)
        else:
            return self._getdir('$HOME', '.local', 'share', self.appname)

    @property
    def config(self):
        if self.__config:
            return self._getdir(self.__config, self.appname)
        elif sys.platform == 'win32':
            return self._getdir(os.environ['APPDATA'], self.appname, 'Config')
        elif sys.platform == 'darwin':
            return self._getdir('$HOME', 'Library', 'Preferences', self.appname)
        else:
            return self._getdir('$HOME', '.config', self.appname)

    @property
    def cache(self):
        if self.__cache:
            return self._getdir(self.__cache, self.appname)
        elif sys.platform == 'win32':
            return self._getdir(os.environ['APPDATA'], self.appname, 'Cache')
        elif sys.platform == 'darwin':
            return self._getdir('$HOME', 'Library', 'Caches', self.appname)
        else:
            return self._getdir('$HOME', '.cache', self.appname)

    def makedirs(self):
        if not os.path.exists(self.data):
            os.makedirs(self.data)
        if not os.path.exists(self.config):
            os.makedirs(self.config)
        if not os.path.exists(self.cache):
            os.makedirs(self.cache)
