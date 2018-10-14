from __future__ import print_function

import sys
from os import path

try:
    from setuptools import setup
except ImportError:
    print("libestg9s4a needs setuptools.", file=sys.stderr)
    print("Please install it using your package-manager or pip.", file=sys.stderr)
    sys.exit(1)

setup(
    name='libestg9s4a',
    version='0.0.1',
    description='',
    author='uberspace.de',
    author_email='hallo@uberspace.de',
    url='https://github.com/uberspace/libestg9s4a',
    long_description=open(path.abspath(path.dirname(__file__)) + '/README.rst').read(),
    long_description_content_type='text/x-rst',
    packages=[
        'libestg9s4a',
    ],
    install_requires=[
        'dataclasses',
    ],
    extras_require={
        'dev': [
            # linting
            'pylava==0.2.*',
            'isort==4.3.*',
            # testing
            'pytest==3.8.*',
            'pytest-cov',
            'tox',
            'codecov',
            # releasing
            'twine',
            # documenting
            'sphinx',
            'sphinx-autobuild',
            'sphinx-autodoc-typehints',
            'sphinx_rtd_theme',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Office/Business :: Financial',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
    zip_safe=True,
)
