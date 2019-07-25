# python import modules

## import module styles

```py
"""Illustration of good import statement styling.

Note that the imports come after the docstring.

"""

# Standard library imports
import datetime
import os

# Third party imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Local application imports
from local_module import local_class
from local_package import local_function

```

### absolute-import

```py
from package2.subpackage1.module5 import function2
from package2 import class1
from package1.module2 import function1
from package1 import module1

```

### relative-import

```py
from .some_module import some_class
from ..some_package import some_function
from . import some_class

from .module2 import function1

from . import class1 # importing a package essentially imports the package’s __init__.py file as a module.
from .subpackage1.module5 import function2 # module in the subpackage1 dir of current dir.
```
