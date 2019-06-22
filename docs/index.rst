
Welcome to pyKirara's documentation!
====================================

pyKirara is a Python library for the `starlight.kirara <https://starlight.kirara.ca>`__ API

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api

Usage
-----

.. code:: python

    import pyKirara

    client = pyKirara.Kirara()
    uzuki = client.get_idol(101)

    print(f"HI! MY NAME IS {uzuki.conventional}")
    print("I'll do my best!")
    print(f"I'am {uzuki.age} years old!")

    # Returns:
    # HI! MY NAME IS Shimamura Uzuki
    # I'll do my best!
    # I'am 17 years old!

Requirements
------------

-  Python 3.5+
-  `Requests <https://github.com/kennethreitz/requests>`__ library

Table of Contents
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
