# Ignore the annoying Cython warnings in PyPy 6

If you install any Cython-based module in PyPy 6.0.0, it is very likely that
you get a warning like this:

```
>>>> import numpy
/data/extra/pypy/6.0.0/site-packages/numpy/random/__init__.py:99: UserWarning: __builtin__.type size changed, may indicate binary incompatibility. Expected 888, got 408
  from .mtrand import *
```

