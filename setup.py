from setuptools import setup, find_packages

import configbetter

with open('README.md') as fh:
    long_desc = fh.read() 

setup(
    name="config-better",
    version="0.1.0",
    description=
    "Configure your application in a friendlier and more consistent way!",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    license="MIT",
    url="https://github.com/kade-robertson/config-better",
    keywords="config better xdg directory",
    author="Kade Robertson",
    author_email="kade@kaderobertson.pw",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=2.7.3, !=3.0.*, !=3.1.*, !=3.2.*')
