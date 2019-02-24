.. pyKirara documentation master file, created by
   sphinx-quickstart on Sun Feb 24 00:22:05 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyKirara's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
pyKirara is a Python library for the starlight.kirara REST API

Usage
-----

.. code:: python

    import pyKirara

    uzuki = pyKirara.Idol(101)

    print(f"HI! MY NAME IS {uzuki.conventional}")
    print("I'll do my best!")
    print(f"I'am {uzuki.age} years old!")

    # Returns:
    # HI! MY NAME IS Shimamura Uzuki
    # I'll do my best!
    # I'am 17 years old!

Requirements
------------

-  Python 3.6 (Will make backwards compatible)
-  `Requests <https://github.com/kennethreitz/requests>`__ library

Table of Contents
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
