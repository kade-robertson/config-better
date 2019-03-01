from setuptools import setup, find_packages

import src

long_desc = ""
try:
    import pypandoc
    long_desc = pypandoc.convert(
        'README.md', 'rst', extra_args=('--eol', 'lf'))
except (IOError, ImportError):
    long_desc = open('README.md').read()

setup(
    name="config-better",
    version="1.0.0",
    description=
    "Configure your application in a friendlier and more consistent way!",
    long_description=long_desc,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    license="MIT",
    keywords="config better xdg directory",
    author="Kade Robertson",
    author_email="kade@kaderobertson.pw",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=2.7.3, !=3.0.*, !=3.1.*, !=3.2.*')
