import pandas as pd  # pandas 1.0.0 version

print(pd.NA & False)
# False

print(pd.NA & True)
# <NA>

print(pd.NA | False)
# <NA>

print(pd.NA | True)
# True
