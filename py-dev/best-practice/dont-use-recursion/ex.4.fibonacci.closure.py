def fib_closure(n):
    f = fib()
    for i in range(2, n+1):
        num = f()
    return num

# %timeit fib_closure(20)
