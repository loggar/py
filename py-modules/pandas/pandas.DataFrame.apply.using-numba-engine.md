# panda

## DataFrame.apply() method can use Numba engine

```py
import pandas as pd #pandas 1.0.0 version

data = pd.Series(range(1_000_000))
roll = data.rolling(10)

def f(x):
    return np.sum(x) + 5

```

```py
# IMPROVEMENTS
# Running in Jupyter Notebook
# Run the first time, compilation time will affect performance
In [4]: %%timeit -r 1 -n 1
        roll.apply(f, engine='numba', raw=True)
Out [4]: 1.23 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

# Function is cached and performance will improve
In [5]: %%timeit
        roll.apply(f, engine='numba', raw=True)
Out [5]: 188 ms ± 1.93 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [6]: %%timeit
        roll.apply(f, engine='cython', raw=True)
Out [6]: 3.92 s ± 59 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
