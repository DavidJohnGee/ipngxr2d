# Copyright 2014 David Gee (@davidjohngee)

from setuptools import setup, find_packages
from distutils.command.install import install as _install

import sys
import platform

if not sys.version_info[0] == 2:
    print "Sorry, Python 3 is not supported (yet)"
    exit()

if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    print "Sorry, Python < 2.6 is not supported"
    exit()

setup(name='ipngxr2d',
      version='0.1',
      description="Python XML parsing utility returning dictionary of children (uses lxml)",
      long_description = "Python XML utility for returning a dictionary of dictionaries from XML children.",
      author="David Gee",
      author_email="david.gee@ipengineer.net",
      url="https://github.com/DavidJohnGee/ipngxr2d",
      packages=find_packages('.'),
      license="Apache License 2.0",
      platforms=["Posix; OS X; Windows"],
      keywords=('XML Parser'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Networking',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ]
      )