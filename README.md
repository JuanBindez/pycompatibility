# pycompatibility


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