#!/usr/bin/env python

from setuptools import setup, find_packages

import pikka_bird_server


setup(
    name     = 'pikka-bird-server',
    version  = pikka_bird_server.__version__,
    packages = find_packages(),
    scripts  = ['bin/pikka-bird-server'],
    
    author       = 'tiredpixel',
    author_email = 'tp@tiredpixel.com',
    description  = "Pikka Bird ops monitoring tool Server component.",
    license      = 'MIT',
    keywords     = 'monitoring',
    url          = 'https://github.com/tiredpixel/pikka-bird-server-py',
    
    install_requires = [
    ]
)
