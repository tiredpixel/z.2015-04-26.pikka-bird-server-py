#!/usr/bin/env python

from setuptools import setup, find_packages

import pikka_bird_server


setup(
    name     = 'pikka-bird-server',
    version  = pikka_bird_server.__version__,
    
    include_package_data = True,
    packages             = find_packages(),
    scripts              = [
        'bin/pikka-bird-server'],
    
    author       = 'tiredpixel',
    author_email = 'tp@tiredpixel.com',
    classifiers  = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    description  = "Pikka Bird ops monitoring tool Server component.",
    keywords     = 'ops monitoring sysadmin',
    license      = 'MIT',
    url          = 'https://github.com/tiredpixel/pikka-bird-server-py',
    
    install_requires = [
        'Flask',
        'Flask-Migrate',
        'Flask-Script',
        'Flask-SQLAlchemy',
        'gunicorn',
        'msgpack-python',
        'psycopg2',
    ]
)
