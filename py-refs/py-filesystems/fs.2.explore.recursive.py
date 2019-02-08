import os

# If you want to get all files and directories recursively, you can do that with the os.walk() function
for (dirpath, dirnames, filenames) in os.walk('./py-dev'):
    for f in filenames:
        print('FILE :', os.path.join(dirpath, f))
    for d in dirnames:
        print('DIRECTORY :', os.path.join(dirpath, d))
