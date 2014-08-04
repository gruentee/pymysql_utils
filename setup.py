import multiprocessing
from setuptools import setup, find_packages
import os
import glob

datafiles = ['pymysql_utils/data/ipToCountrySoftware77DotNet.csv']

setup(
    name = "pymysql_utils",
    version = "0.50",
    packages = find_packages(),

    # Dependencies on other packages:
    # Couldn't get numpy install to work without
    # an out-of-band: sudo apt-get install python-dev
    setup_requires   = [],
    install_requires = [#'pymysql3>=0.5',
                        'MySQL-python>=1.2.5',
			'configparser>=3.3.0'
			],
    tests_require    = ['sentinels>=0.0.6', 'nose>=1.0'],

    # Unit tests; they are initiated via 'python setup.py test'
    test_suite       = 'nose.collector', 

    data_files = [('pymysql_utils/data', datafiles)],


    # metadata for upload to PyPI
    author = "Andreas Paepcke",
    author_email = "paepcke@cs.stanford.edu",
    description = "Thin wrapper around pymysql. Provides Python iterator for queries. Abstracts away cursor.",
    license = "BSD",
    keywords = "MySQL",
    url = "https://github.com/paepcke/pymysql_utils",   # project home page, if any
)
