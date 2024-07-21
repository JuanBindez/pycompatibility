# pycompatibility

![PyPI - Downloads](https://img.shields.io/pypi/dm/pycompatibility)
![PyPI - License](https://img.shields.io/pypi/l/pycompatibility)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/pycompatibility?include_prereleases)
<a href="https://pypi.org/project/pycompatibility/"><img src="https://img.shields.io/pypi/v/pycompatibility" /></a>

## Python3 library for checking code compatibility with different Python versions.


### Install

    pip install pycompatibility

### test code:

```python
from pycompatibility import CompatibilityChecker

checker = CompatibilityChecker("script.py")
checker.verify()

```

### command line just pass the name of the script as an argument which will show compatibility

    pycompatibility script.py
