import pandas as pd  # pandas 1.0.0 version

s = pd.Series([1, 2, None], dtype="Int64")

print(s)

print(type(s[2]))  # pandas._libs.missing.NAType
