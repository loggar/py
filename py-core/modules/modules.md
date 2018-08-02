Ref)

https://www.tutorialspoint.com/python3/python_modules.htm

## The globals() and locals() Functions

The globals() and locals() functions can be used to return the names in the global and local namespaces depending on the location from where they are called.

* If locals() is called from within a function, it will return all the names that can be accessed locally from that function.

* If globals() is called from within a function, it will return all the names that can be accessed globally from that function.

The return type of both these functions is dictionary. Therefore, names can be extracted using the keys() function.

## The reload() Function

When a module is imported into a script, the code in the top-level portion of a module is executed only once.

Therefore, if you want to reexecute the top-level code in a module, you can use the reload() function. The reload() function imports a previously imported module again. The syntax of the reload() function is this −

```
reload(module_name)
```

## Packages in Python

A package is a hierarchical file directory structure that defines a single Python application environment that consists of modules and subpackages and sub-subpackages, and so on.

Consider a file Pots.py available in Phone directory. This file has the following line of source code −

```
#!/usr/bin/python3

def Pots():
print ("I'm Pots Phone")
```

Similar, we have other two files having different functions with the same name as above. They are −

* Phone/Isdn.py file having function Isdn()
* Phone/G3.py file having function G3()

Now, create one more file `__init__.py in the Phone directory −

* `Phone/__init__.py`

To make all of your functions available when you have imported Phone, you need to put explicit import statements in `__init__.py` as follows −

```
from Pots import Pots
from Isdn import Isdn
from G3 import G3
```

After you add these lines to `__init__.py`, you have all of these classes available when you import the Phone package.

```
#!/usr/bin/python3

# Now import your Phone Package.
import Phone

Phone.Pots()
Phone.Isdn()
Phone.G3()
```

When the above code is executed, it produces the following result −

```
I'm Pots Phone
I'm 3G Phone
I'm ISDN Phone
```
