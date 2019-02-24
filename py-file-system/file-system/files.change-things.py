import os
import shutil

os.chdir("./_tmp/dir1")  # cd
os.path.join("dir2", "dir3")
os.sep
os.makedirs("./dir2/dir3")

shutil.copy2("./dir1/file1", "./dir2")
shutil.move("./dir1/file2", "./dir2")

os.remove("./dir1/file3")
shutil.rmtree("./dir1/dir4")

# shutil.rmtree() removes a directory and all files and directories in it.
