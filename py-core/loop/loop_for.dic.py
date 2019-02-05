d = {'foo': 1, 'bar': 2, 'baz': 3}

for k in d:
    print(k)

for k in d:
    print(d[k])

for v in d.values():
    print(v)


for k, v in d.items():
    print('k =', k, ', v =', v)
