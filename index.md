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



Unit tests: pytest
------------------

~~~~ text
$ pip install pytest
~~~~

`tests/test_wordcount.py`:

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

`pytest` heeft handige helpers, `pyhamcrest`¹ maakt één en ander leesbaarder:

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

----

¹: importeer uit module `hamcrest`



Unit tests
----------

![thumbs up](assets/thumbs-up.svg)


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



Documentatie: PyCharm
---------------------

![Spinx in PyCharm](assets/new-docs-runner.png)



Documentatie: PyCharm
---------------------

![Spinx in PyCharm](assets/docs-runner.png)



Documentatie
------------

![thumbs up](assets/thumbs-up.svg)
