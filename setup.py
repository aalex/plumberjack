#!/usr/bin/env python
"""
setup.py for Plumberjack

To update the version number : 
vim -o pyoscape/__init__.py
"""
from setuptools import setup
import sys
import plumberjack

setup(
    name="plumberjack",
    version=plumberjack.__version__,
    description="Python interface to jack audio connection kit",
    author="SAT",
    author_email="alexandre@quessy.net",
    # not yet created
    url="http://github.com/sat-metalab/plumberjack",
    packages=['plumberjack'],
    scripts=[]
    )
