Python alsof het *echte* software is
====================================

![DUPLO](assets/duplo.svg)



Hoezo?!
-------

- FBDA's weapon of choice
- zowel losse scripts  als 'libs'
- herbruikbaarheid non-triviaal
- geringe ervaring met tooling
- impulsgroep DUPLO™


Invulling
---------

- typisch los script (doet het!): `wordcount.py`
- nou nog herbruikbaar…
- spelen met veelgebruikte tooling
    - `pytest`, `setuptools`, `sphinx`, `tox`, `wheel`, …
    - PyCharm



Not Invented Here™
------------------

- github's trending python projects als inspiratie (`keras`, `requests`, …)
- project-layout (`test_dingen.py` of `tests/test_iets.py`, …)
- gebruikte tools (`pytest` of `unittest2`, …)



TODO
----

- `virtualenv`
- documentatie met `sphinx`
- unittests met `pytest`
- packaging met `setuptools` en `wheel`
- automatisering met `tox`
- eventueel
    - 'lint' met `flake8`
    - coverage met `coverage`



Woordjes tellen
---------------

- live meeklikken (of kopie-pasta): `https://akaidiot.github.com/word-count/`

~~~~ text
$ git clone https://github.com/akaIDIOT/word-count.git
$ python3 wordcount.py map/met/tekst
[('de', 123), ('het', 45), ('een', 6)]
~~~~

- PyCharm
- `virtualenv`



Documentatie: Spinx
----------------------

Krachtige tool, maar veel TLC nodig…

~~~~ text
$ pip install sphinx
$ cd …/word-count
$ sphinx-quickstart
> Root path for the documentation [.]: docs
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> Create Makefile? (y/n) [y]: n
> Create Windows command file? (y/n) [y]: n
~~~~



Documentatie: `conf.py`
----------------------

~~~~ python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
~~~~



Documentatie: `index.rst`
-------------------------

~~~~ rest
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
~~~~



Documentatie: `api.rst`
-----------------------

~~~~ rest
API Docs
========

.. automodule:: wordcount
   :members:
   :undoc-members:
~~~~

Niet per se fijn, eventueel in `conf.py`:

~~~~ python
autodoc_default_flags = ['members', 'undoc-members']
~~~~

Zie [Sphinx' `autodoc` doc](http://www.sphinx-doc.org/en/stable/ext/autodoc.html) voor meer