#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(name='metatron-network',
      version='1.0.0',
      description='Python implementation of Metatron Deep Belief Networks',
      packages=['dbn', 'dbn.tensorflow'],
      install_requires=requirements,
      )