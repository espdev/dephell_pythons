# Dephell Pythons

Work with python versions.

## Installation

Install from [PyPI](https://pypi.org/project/dephell-pythons/):

```bash
python3 -m pip install --user dephell_pythons
```

## Usage

```python
from dephell_pythons import Pythons

pythons = Pythons()

# get current:
python = pythons.get_best()

# properties:
python.name     # 'python3.7'
python.path     # Path('/usr/local/bin/python3.7')
python.version  # <Version('3.7.0')>

# get by version
pythons.get_best('3.5').version
# <Version('3.5.2')>

# get by name
pythons.get_best('python3').version
# <Version('3.6.7')>

# get by specifier
pythons.get_best('<3.7').version
# <Version('3.6.7')>

# get by path
pythons.get_best('/usr/bin/python3.6').version
# <Version('3.6.7')>

# get all
list(pythons)
# [Python(...), Python(...), ...]

# work not only with installed pythons:
Pythons(abstract=True).get_best('>=2.8,<3.5').version
# <Version('3.4')>
```
