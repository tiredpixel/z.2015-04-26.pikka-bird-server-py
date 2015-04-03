#!/usr/bin/env python

from setuptools import setup, find_packages

import pikka_bird_receiver


setup(
    name     = 'pikka-bird-receiver',
    version  = pikka_bird_receiver.__version__,
    packages = find_packages(),
    scripts  = [],
    
    author       = 'tiredpixel',
    author_email = 'tp@tiredpixel.com',
    description  = "Pikka Bird monitoring tool metrics receiver.",
    license      = '',
    keywords     = 'monitoring',
    url          = '',
    
    install_requires = [
    ]
)
