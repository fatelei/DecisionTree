#!/usr/bin/python
#-*-coding: utf8-*-

from setuptools import find_packages, setup

install_requires = []

entry_points = """
    [console_scripts]
    destree=DesTree.app:run
"""

setup(
    author='fatelei@gmail.com',
    version='0.1',
    name='decstree',
    install_requires=install_requires,
    entry_points=entry_points,
    packages=find_packages('apps'),
    package_dir={'': 'apps'}
    )