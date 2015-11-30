#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='lazyconfig',
    version='0.1',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    maintainer='Alexandre Vicenzi',
    maintainer_email='vicenzi.alexandre@gmail.com',
    packages=['lazyconfig'],
    url='https://github.com/alexandrevicenzi/lazyconfig',
    bugtrack_url='https://github.com/alexandrevicenzi/lazyconfig/issues',
    license='MIT',
    description='Yaml configuration made lazy',
    long_description='Yaml configuration made lazy',
    keywords='yaml, configuration, setup',
    install_requires=['PyYAML>=3.11'],
    platforms='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Utilities',
    ],
)
