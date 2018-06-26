#!/usr/bin/python3
import os

# Create a directory "test"
os.mkdir("./dist/testdir")

# Changing a directory to "./dist/testdir"
os.chdir("./dist")

# This would give location of the current directory
cwd = os.getcwd()
print(cwd)

# This would  remove "./dist/testdir"  directory.
os.rmdir("./testdir")
