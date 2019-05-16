import shutil
import os

shutil.copy('C:\\spam.txt', 'C:\\delicious')

shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')

shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

shutil.move('C:\\bacon.txt', 'C:\\eggs')

shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')

shutil.move('C:\\bacon.txt', 'C:\\eggs')

shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
