import zipfile
import os


os.chdir('C:\\')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()

spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size

'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
                                           .compress_size, 2))

exampleZip.close()
