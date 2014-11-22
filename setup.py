#!/usr/bin/env python
from setuptools import setup
import os
import sys

setup(
    name='cythonrun',
    version='0.1.0',
    author='Andreas Bunkahle',
    author_email='abunkahle@t-online.de',
    description='compile and run cython in one line',
    license='MIT',
    url='https://github.com/bunkahle/cythonrun',
    long_description='https://github.com/bunkahle/cythonrun',
    platforms = ['any'],
    install_requires=['setuptools', 'cython'],
    scripts = ['runcython.py', 'cythonrun.py', 'makecython.py'],
)
