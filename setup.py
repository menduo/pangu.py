#!/usr/bin/env python
# coding: utf-8

import os
import sys

from setuptools import setup


def get_version():
    code = None
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'pangu.py',
    )
    with open(path) as f:
        for line in f:
            if line.startswith('__version__'):
                code = line[len('__version__ = '):]
                break
    return eval(code)


if sys.argv[-1] == 'wheel':
    os.system('make clean')
    os.system('pip install wheel')
    os.system('python setup.py bdist_wheel')
    sys.exit(0)

if sys.argv[-1] == 'publish':
    os.system('python setup.py wheel')
    os.system('pip install twine')
    os.system('twine upload dist/*')
    sys.exit(0)

long_description = open('README.rst').read() + '\n' + open('HISTORY.rst').read()

setup(
    name='pangu',
    version=get_version(),
    description='Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits and symbols).',
    long_description=long_description,
    keywords='pangu space white text spacing readability',
    author='Vinta Chen',
    author_email='vinta.chen@gmail.com',
    url='https://github.com/vinta/pangu.py',
    license='MIT',
    include_package_data=True,
    py_modules=['pangu', ],
    scripts=['bin/pangu', ],
    test_suite='test_pangu',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Japanese',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Education',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ),
)
