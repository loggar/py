import os
import send2trash

for filename in os.listdir():
    if filename.endswith('.rxt'):
        # os.unlink(filename)
        print(filename)


# Safe Deletes with the send2trash Module

baconFile = open('bacon.txt', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

send2trash.send2trash('bacon.txt')
