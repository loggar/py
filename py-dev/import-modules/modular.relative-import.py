from .some_module import some_class
from ..some_package import some_function
from . import some_class

from .module2 import function1

from . import class1 # importing a package essentially imports the package’s __init__.py file as a module.
from .subpackage1.module5 import function2 # module in the subpackage1 dir of current dir.