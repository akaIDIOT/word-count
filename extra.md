word-count extra's
==================



Argumenttypes
=============

- bestandsnaam / fileobj / line iterator?
	- testen met files wordt snel irritant
- is dat type wat je hebt gemaakt hier *echt* voor nodig?
	- vaak is een `callable` al genoeg
- moet dit per se een `DataFrame` zijn?
	- `list` en `dict` zijn vrij capabel



'Side effects'
==============

- testbaarheid, herbruikbaarheid
	- 'separation of concerns'

- `print()` (dus ook `tqdm` ☺)
- read + write

- niet zwart wit:
	- read + transform / filter (kan uiteraard prima los)

`wordcount.py`
--------------

- `print`
- `counts[:top]`



Performance
===========

- file descriptors
- *alles* in geheugen → generators / iterators
- wanneer maakt zoiets nou uit?
- `threading` / `multiprocessing` / `concurrent.futures` / `ascynio` / `joblib` ?

`wordcount.py`
--------------

- `for f in files: open(f)`
- `source += f.read()`
- `if key not in data: data[key] = value`



Dependencies
============

- forceert dingen bij gebruikers
- is `pandas` hier echt nodig?
- abandonware / versies / python3 fork



Geleverd *met* batterijen!
==========================

- `argparse`
- `collections`
- `functools` / `itertools`
- `pathlib`
- `shutil`
- …

`wordcount.py`
--------------

- argument parser
- `counts = Counter()`
