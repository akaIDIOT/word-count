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
- verder: "populaire conventie"


What TODO
---------

- `virtualenv`
- unittests met `pytest`
- packaging met `setuptools` en `wheel`
- documentatie met `sphinx`
- automatisering met `tox`
- eventueel
    - 'lint' met `flake8`
    - test/code coverage met `coverage`



Requirements
------------

- `git --version`
- `python3 --version`
- `pip --version` (verwijst naar welke versie van Python?)
    - eventueel `pip3`
- `pip show pip`
- PyCharm (community of professional)



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



Virtual reality
---------------

Alle DUPLO-blokken netjes in de doos:

~~~~ text
$ pip install virtualenv
$ virtualenv --python python3 pad/naar/env
$ source pad/naar/env/activate   # *nix
$ pad\naar\env\Scripts\activate  # windows
~~~~



Virtual reality: PyCharm
------------------------

![interpreter in PyCharm](assets/project-interpreter.png)



Virtual reality
---------------

![thumbs up](assets/thumbs-up.svg)



Unit tests
----------

- een 'unit' is klein
- `wordcount.py` is niet handig testbaar ☹ (één unit)
- eerst fixen of eerst tests maken?
    - pragmatisme of test driven development

*populaire conventie: test-code in `…/tests/`*



Unit tests: pytest
------------------

~~~~ text
$ pip install pytest
~~~~

`…/tests/test_wordcount.py`:

~~~~ python
def test_tokenize():
    text = 'De kat krabt de krullen van de trap.'
    words = tokenize(text)

    assert 'krullen' in words
    assert 'trap' in words
~~~~



Unit tests: PyCharm
-------------------

![pytest in PyCharm](assets/test-runner.png)

Rechts-klik op `tests`, ▶ Run 'py.test in tests'



Bonus tests
-----------

`pytest` heeft handige helpers, `pyhamcrest`[^1] maakt één en ander leesbaarder:

~~~~ python
@pytest.mark.parametrize('text, words', [
    ('test', ['test']),
    ('testing\n123', ['testing', '123']),
])
def test_tokenize(text, words):
    assert_that(tokenize(text),
                contains_inanyorder(*words))
~~~~

`mock` / `unittest.mock` kan dingen die in de weg zitten (HTTP-requests, database-cursors, …) 'mocken'

[^1]: importeer uit module `hamcrest`



Unit tests
----------

![thumbs up](assets/thumbs-up.svg)



Packaging
---------

- pakketje wat Python 'snapt'
- Python packages, modules *en dependencies*

*(niet alleen) populaire conventie: `…/setup.py`*



Packaging: `setup.py`
---------------------

~~~~ python
from setuptools import setup


setup(
    name='wordcount',
    version='0.0',             # see PEP-440
    description='Count words, duh',
    author='Henk de Vries',
    author_email='henk.de.vries@nfi.minvenj.nl',
    py_modules=['wordcount'],  # single module
    install_requires=[],       # no dependencies
)
~~~~



Packaging: `wordcount.tar.gz`
-----------------------------

~~~~ text
$ python setup.py bdist
$ ls dist/
wordcount-0.0.linux-x86_64.tar.gz
~~~~

euh… `x86_64`? `.tar.gz`? ☹



Packaging: `wordcount.whl`
--------------------------

~~~~ text
$ pip install wheel
$ python setup.py bdist_wheel
$ ls dist/
wordcount-0.0-py3-none-any.whl
~~~~

oeh, `py3-none-any`, `.whl` ☺



Packaging: `pip install wordcount`
----------------------------------

- afdeling heeft een PyPI-server (😘 FIG)
- iedereen heeft leesrechten
- schrijfrechten op aanvraag
- configuratie op confluence

~~~~ text
$ twine upload --repository dbs dist/*.whl
~~~~



Packaging
---------

![thumbs up](assets/thumbs-up.svg)



Documentatie: Spinx
-------------------

- krachtige tool, maar veel TLC nodig…
- geconfigureerd in Python
- genereert documentatie vanaf `index.rst`
- reStructuredText (☹)
- importeert code, rendert docstrings zoals bijv. *readthedocs.org*



Documentatie: Sphinx
--------------------

~~~~ text
$ pip install sphinx
$ cd …/word-count
$ sphinx-quickstart
> Root path for the documentation [.]: docs
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> Create Makefile? (y/n) [y]: n
> Create Windows command file? (y/n) [y]: n
~~~~

*populaire conventie: doc root in `…/docs/`*



Documentatie: `conf.py`
----------------------

vies, maar hier nodig…

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



Documentatie: PyCharm
---------------------

![Spinx in PyCharm](assets/new-docs-runner.png)



Documentatie: PyCharm
---------------------

![Spinx in PyCharm](assets/docs-runner.png)



Documentatie
------------

![thumbs up](assets/thumbs-up.svg)
