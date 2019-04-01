# config-better

![CircleCI Build Status](https://img.shields.io/circleci/token/a23936ed1748d98b98003357c1e205619209af66/project/github/kade-robertson/config-better/master.svg?style=flat-square) ![Codecov](https://img.shields.io/codecov/c/github/kade-robertson/config-better.svg?style=flat-square)

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

```bash
pip install config-better
```

## Developing

1. Clone the repo
2. `git checkout -b some-feature-or-bugfix`
3. Do work
4. Test with `python setup.py test` (add if necessary)
5. Run `yapf -ir .` and `isort` to standardize.
6. Make a PR.
