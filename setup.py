#!/usr/bin/env python

from setuptools import setup, find_packages

import pikka_bird_server


setup(
    name     = 'pikka-bird-server',
    version  = pikka_bird_server.__version__,
    packages = find_packages(),
    scripts  = [],
    
    author       = 'tiredpixel',
    author_email = 'tp@tiredpixel.com',
    description  = "Pikka Bird monitoring tool Server component.",
    license      = '',
    keywords     = 'monitoring',
    url          = '',
    
    install_requires = [
    ]
)
