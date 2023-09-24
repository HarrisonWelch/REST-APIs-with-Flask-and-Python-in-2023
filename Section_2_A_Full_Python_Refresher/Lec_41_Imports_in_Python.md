# Imports in Python

How to work with files and how to get code into another file

```py
def divide(dividend, divisor):
    return dividend / divisor

print("mymodule.py", __name__)
# > mymodule.py __main__
```

Import this

```py
from mymodule import divide
```

or all of it

```py
import mymodule
```

Run the code from mymodule

```py
from mymodule import divide

print(divide(10, 2))

# > mymodule.py mymodule
# > 5.0
```

Notice that **name** gives the module name "mymodule" and not "**main**" anymore. That is b/c only the file you run is under "main"

Code.py

```py
...
print(__name__)
# > __main__
```

How does this work? The answer is in `import sys`

```py
print(sys.path)
```

This gives a list of paths for searching for modules

This list looks like this
* C:\...\...\REST_APIs_with_Flask_and_Python_in_2023\Section_2_A_Full_Python_Refresher\29_imports_in_python
* C:\...\AppData\Local\Programs\Python\Python311\python311.zip
* C:\...\AppData\Local\Programs\Python\Python311\DLLs
* C:\...\AppData\Local\Programs\Python\Python311\Lib
* C:\...\AppData\Local\Programs\Python\Python311
* C:\...\AppData\Local\Programs\Python\Python311\Lib\site-packages

Basically python install location plus the active directory

In Linux systems you can use `export PYTHONPATH = /Users` and then you'll see the python path in the list of sys.path as well.

## Multi-layer import

code.py
```py
import mymodule
```

mymodule.py
```py
def divide(dividend, divisor):
    return dividend / divisor

print("mymodule.py", __name__)

import libs.mylib
```

mylib.py
```py
print("mylib.py", __name__)
```

Output

```
mymodule.py mymodule
mylib.py libs.mylib
```

Python 2 will need to see a __init__.py in the dir that is importing.

Python keeps track of what has been imported to avoid double importing.

Use `print(sys.modules)` to see all imported modules.
