# -*- coding: utf-8 -*-
"""
"""
import os
import re
from setuptools import setup, find_packages

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.join(ROOT_PATH, 'seemslegit')


def get_version():
    filename = os.path.join(PROJECT_PATH, '__init__.py')
    with open(filename) as f:
        contents = f.read()
    pattern = r"^__version__ = ['\"]([^'\"]*)['\"]$"
    match = re.search(pattern, contents, re.MULTILINE)
    if match:
        return match.group(1)
    raise RuntimeError('Unable to find version string in {}'.format(filename))


setup(
    name='seemslegit',
    version=get_version(),
    url='http://github.com/vaiski/seemslegit',
    license='MIT',
    author=u'Eemil Väisänen',
    author_email='eemil.vaisanen@iki.fi',
    description='',
    long_description=__doc__,
    packages=find_packages('.', exclude=('tests', 'tests.*')),
    package_data={
        'seemslegit.config': ['*.ini']
    },
    install_requires=[
        'six',
    ],
    extras_require={
        'test': [
            'pytest',
            'pylint',
            'flake8'
        ]
    },
    test_suite='tests',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
