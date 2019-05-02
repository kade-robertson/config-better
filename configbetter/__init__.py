"""
Handles all of the logic for config-better.
"""

import os
import shutil
import sys


def _getdir(*pathparts) -> str:
    return os.path.expandvars(os.path.join(*pathparts))


class Config:
    """
    Provides functionality to determine & create directories.
    """

    def __init__(self, appname: str, force_unix: bool = False):
        """
        Creates a Config object.
        
        This also pulls in environment data related to the XDG Base Directory
        specification.

        Arguments:
            appname {str} -- The name that will be used when deciding the
                             folders to be used for data, config and cache.
            force_unix {bool} -- If desired, you can force this to only use
                                 Unix-like paths even on Windows/Darwin.
                                 This does not take effect if XDG_ vars are
                                 set.
        """

        self.appname = appname
        self.force_unix = force_unix
        self.__data = None
        self.__config = None
        self.__cache = None
        if 'XDG_DATA_HOME' in os.environ:
            self.__data = os.environ['XDG_DATA_HOME']
        if 'XDG_CONFIG_HOME' in os.environ:
            self.__config = os.environ['XDG_CONFIG_HOME']
        if 'XDG_CACHE_HOME' in os.environ:
            self.__cache = os.environ['XDG_CACHE_HOME']

    @property
    def data(self) -> str:
        """
        Provides the data folder the application should use. 
        
        To follow the XDG Base Directory specification, it first checks whether
        the XDG_DATA_HOME environment variable has been set.

        If set:
         - The data directory should be $XDG_DATA_HOME/appname

        Otherwise, it is platform dependent:
         - Windows: $APPDATA/appname/Data
         - Mac OS: $HOME/Library/appname
         - Linux/Other: $HOME/.local/share/appname

        Returns:
            str -- The full path to the preferred data folder.
        """

        if self.__data:
            return _getdir(self.__data, self.appname)
        if sys.platform == 'win32' and not self.force_unix:
            return _getdir(os.environ['APPDATA'], self.appname, 'Data')
        if sys.platform == 'darwin' and not self.force_unix:
            return _getdir('$HOME', 'Library', self.appname)
        return _getdir('$HOME', '.local', 'share', self.appname)

    @property
    def config(self) -> str:
        """
        Provides the config folder the application should use.
        
        To follow the XDG Base Directory specification, it first checks whether
        the XDG_CONFIG_HOMEenvironment variable has been set.

        If set:
         - The data directory should be $XDG_CONFIG_HOME/appname

        Otherwise, it is platform dependent:
         - Windows: $APPDATA/appname/Config
         - Mac OS: $HOME/Library/Preferences/appname
         - Linux/Other: $HOME/.config/appname

        Returns:
            str -- The full path to the preferred config folder.
        """

        if self.__config:
            return _getdir(self.__config, self.appname)
        if sys.platform == 'win32' and not self.force_unix:
            return _getdir(os.environ['APPDATA'], self.appname, 'Config')
        if sys.platform == 'darwin' and not self.force_unix:
            return _getdir('$HOME', 'Library', 'Preferences', self.appname)
        return _getdir('$HOME', '.config', self.appname)

    @property
    def cache(self) -> str:
        """
        Provides the cache folder the application should use. 
        
        To follow the XDG Base Directory specification, it first checks whether
        the XDG_CACHE_HOME environment variable has been set.

        If set:
         - The data directory should be $XDG_CACHE_HOME/appname

        Otherwise, it is platform dependent:
         - Windows: $APPDATA/appname/Cache
         - Mac OS: $HOME/Library/Caches/appname
         - Linux/Other: $HOME/.cache/appname

        Returns:
            str -- The full path to the preferred cache folder.
        """

        if self.__cache:
            return _getdir(self.__cache, self.appname)
        if sys.platform == 'win32' and not self.force_unix:
            return _getdir(os.environ['APPDATA'], self.appname, 'Cache')
        if sys.platform == 'darwin' and not self.force_unix:
            return _getdir('$HOME', 'Library', 'Caches', self.appname)
        return _getdir('$HOME', '.cache', self.appname)

    def makedirs(self):
        """
        Creates the data, cache, and config folders.

        New directories are only made if they do not already exist.
        """

        if not os.path.exists(self.data):
            os.makedirs(self.data)
        if not os.path.exists(self.config):
            os.makedirs(self.config)
        if not os.path.exists(self.cache):
            os.makedirs(self.cache)

    def rmdirs(self):
        """
        Removes the data, cache and config folders.

        May be useful for uninstall scripts or cleaning scripts. Handles a
        special case for Windows where, in default scenarios, there is a parent]
        directory that needs to be cleared.
        """

        if os.path.exists(self.cache):
            shutil.rmtree(self.cache)
        if os.path.exists(self.config):
            shutil.rmtree(self.config)
        if os.path.exists(self.data):
            shutil.rmtree(self.data)
        windows_dir = _getdir(os.environ['APPDATA'], self.appname)
        if sys.platform == 'win32' and not self.force_unix and not (self.__data or self.__cache
                                            or self.__config) and os.path.exists(windows_dir):
            shutil.rmtree(windows_dir)
