import pandas as pd  # pandas 1.0.0 version

df = pd.DataFrame(data={"col_1": ["a", "b"], "col_2": ["c", "d"]})

print(df.to_markdown())
