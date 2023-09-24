# Relative imports in Python

code.py

```py
import mymodule

print("code.py:", __name__)
```

mymodule

```py
from libs import mylib

print("mymodule.py:", __name__)
```

mylib.py

```py
from libs.operations import operator

print("mylib.py:", __name__)
```

operator.py

```py
print("operator.py: ", __name__)
```

![30_file_org image]()

Output

```
operator.py:  libs.operations.operator
mylib.py: libs.mylib
mymodule.py: mymodule
code.py: __main__
```

Notice on run that the imports are all reverse. The deepest file runs first.

## Relative input

Put a function in mymodule.py
```py
...
def divide():
    pass
```

Then import in code.py

```py
# import mymodule
from .mymodule import divide
...
```

You get `ImportError: attempted relative import with no known parent package`

package and folder mean the same thing when talking python source

If you are to use relative imports you need to the keep the same file at the top level.

## Parent folder

`from ..mylib import *` will import what is already in the known modules.

`import *` will import everything.

Advice don't use relative import. Brain hurt.
