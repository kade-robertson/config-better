# config-better

Make use of directories for configuration / data / caching better and more user-friendly!

This module provides support for the XDG Base Directory specification, and OS-friendly fallbacks for Windows, Mac OS, and Linux if not otherwise specified.

## Usage

```python
import os.path
import configbetter

c = configbetter.Config('appname')

with open(os.path.join(c.config, 'config.json')) as conf:
    # ...
```

Available properties of `Config`:

- `.cache`, which points to `$XDG_CACHE_HOME` if available, otherwise uses a generic system equivalent.
- `.config`, which points to `$XDG_CONFIG_HOME` if available, otherwise uses a generic system equivalent.
- `.data`, which points to `$XDG_DATA_HOME` if available, otherwise uses a generic system equivalent.

Additionally, the following method is provided:

- `.makedirs()` will create the cache, config and data directories if they do not already exist, including all parent directories.

## Installation

```
pip install config-better
```