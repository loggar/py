import pathlib

path = pathlib.Path.home()

print(path)

for p in path.iterdir():
    if p.is_file() and p.suffix == '.json':
        print(p.name)

# The same can be done by using the Path.glob() method with one less line:
path = pathlib.Path.home()
print(path)
for p in path.glob('*.json'):
    print(p.name)
