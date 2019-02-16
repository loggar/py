import os

folder = '.'
filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]

print(filepaths)

# os.scandir() function (available for Python >= 3.5 or with the scandir module)
filepaths = [f.path for f in os.scandir('.') if f.is_file()]
dirpaths = [f.path for f in os.scandir('.') if f.is_dir()]

print(filepaths)
print(dirpaths)
