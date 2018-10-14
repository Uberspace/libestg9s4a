libestg9s4a
###########

.. image:: https://travis-ci.com/Uberspace/libestg9s4a.svg?branch=master
    :target: https://travis-ci.com/Uberspace/libestg9s4a
    :alt: CI Status

.. image:: https://readthedocs.org/projects/libestg9s4a/badge/?version=latest
    :target: https://libestg9s4a.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/libestg9s4a.svg
    :target: https://pypi.python.org/pypi/libestg9s4a
    :alt: PyPI

§ 9, section 4a of the German Einkommensteuergesetz (EStG) defines height of
reimbursements on business trips. This library takes the from/to dates of a trip
as well as the already-paid-for meals for each day and returns a list of days
detailing how much must be paid to the employee.

As noted in the license, this software is provided without any warranty or
guarantee for correctness.

Installation
------------

Install libestg9s4a via pip:

.. code-block:: console

    $ pip install libestg9s4a

Usage
-----

.. code-block:: pycon

    >>> import datetime as DT
    >>> from libestg9s4a import EStG9s4a


Development
-----------

Setup
^^^^^

Using python 3.6, do the following:

.. code-block:: console

    $ virtualenv venv --python=python3.6
    $ pip install -e ".[dev]"

Usual Tasks
^^^^^^^^^^^

* ``make test``: run tests (use ``tox`` or ``py.test`` directly to supply flags like ``-k``)
* ``make lint``: run pylava and friends
* ``make fixlint``: sort imports correctly

Releasing a new version
^^^^^^^^^^^^^^^^^^^^^^^

Assuming you have been handed the required credentials, a new version
can be released as follows.

1. adapt the version in ``setup.py``, according to `semver`_.
2. commit this change as ``Version 1.2.3``
3. tag the resulting commit as ``v1.2.3``
4. push the new tag as well as the ``master`` branch
5. update the package on PyPI:

.. code-block:: console

    $ rm dist/*
    $ python setup.py sdist bdist_wheel
    $ twine upload dist/*

Prerequisites
-------------

This library is currently python 3.6+. If you would like to use this library
with a lower python version, please open an issue. We're happy to change things
around.

Versioning
----------

New version numbers are assigned following `semver`_. All
0.x.y versions are tested and usable, but do not have a stable public interface.

A version 1.0 will be released, once we deem the library stable.

License
-------

All code in this repository is licensed under the MIT license.

.. _semver: http://semver.org/
