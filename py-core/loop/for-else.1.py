for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Will not execute


for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'baaaaaaaaaz':
        break
    print(i)
else:
    print('Done.')  # Will execute
