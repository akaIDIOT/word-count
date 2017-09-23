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
- 'lint' met `flake8`



Woordjes tellen
---------------

- live meeklikken (of kopie-pasta): `https://akaidiot.github.com/word-count/`

~~~~
$ git clone https://github.com/akaIDIOT/word-count.git
$ python3 wordcount.py map/met/tekst
[('de', 123), ('het', 45), ('een', 6)]
~~~~

- PyCharm
- `virtualenv`
