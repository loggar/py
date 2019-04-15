# build windows exe file via cx_freeze

```
pip install cx_freeze
```

`setup.py`

```
import sys

from cx_Freeze import setup, Executable

setup(  name = "parser",
        version = "1.0",
        description = "Parser",
        author = "sh1n2",
        executables = [Executable("parser.py")])
        # if GUI executables = [Executable("imgtk.py", base="Win32GUI")])
```

make exe file

```
python setup.py bulid
```

make installation package

```
python setup.py bdist_msi
```
