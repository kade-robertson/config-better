import subprocess

from setuptools import find_packages, setup

import configbetter

with open('README.md') as fh:
    long_desc = fh.read()

version = "1.0.1"
last_commit = subprocess.check_output(["git", "rev-list", "HEAD",
                                       "--count"]).decode('utf-8').strip()
branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref",
                                  "HEAD"]).decode('utf-8').strip()

setup(
    name="config-better",
    version=version + (f".{last_commit}-{branch}" if __debug__ else ""),
    description="Configure your application in a friendlier and more consistent way!",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    url="https://github.com/kade-robertson/config-better",
    keywords="config better xdg directory",
    author="Kade Robertson",
    author_email="kade@kaderobertson.pw",
    packages=find_packages(),
    install_requires=[],
    test_suite='tests',
    python_requires='>=3.6.*')
