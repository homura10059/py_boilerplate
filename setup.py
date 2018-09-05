#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re

from setuptools import setup

PACKAGE_NAME = 'py_boilerplate'

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('py_boilerplate/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name=PACKAGE_NAME,
    version=version,
    url='https://github.com/o-hayato/py_boilerplate',
    license='MIT',
    author='o-hayato',
    author_email='preasper0+github@gmail.com',
    description='python boilerplate',
    long_description=readme,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.4',
    install_requires=[
    ],
    extras_require={
        'dev': [
            'pytest>=3',
            'coverage',
            'tox',
            'sphinx',
            'pallets-sphinx-themes',
            'sphinxcontrib-log-cabinet',
        ],
        'docs': [
            'sphinx',
            'pallets-sphinx-themes',
            'sphinxcontrib-log-cabinet',
        ]
    },
    entry_points='''
        [console_scripts]
        {pkg}={pkg}.cli:main
    '''.format(pkg=PACKAGE_NAME),

)