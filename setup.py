# -*- coding: utf-8 -*-

from distutils.core import setup
from glob import glob
import subprocess

scripts = glob('scripts/*')
command = ['git', 'describe', '--tags']
version = subprocess.check_output(command).decode().strip()

setup(name='config',
      version=version,
      description='Global Configurations',
      author='Shuo Han',
      author_email='shan50@jhu.edu',
      scripts=scripts,
      packages=['config'])
