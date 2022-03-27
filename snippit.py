import pathlib
import os

print(pathlib.Path.cwd())
root_directory = pathlib.Path.home().drive
current_directory = pathlib.Path.cwd()
os.chdir(str(root_directory)+'\\')
print(pathlib.Path.cwd())


def change_directory(new_location):
    os.chdir(new_location)
    current_directory = pathlib.Path.cwd


change_directory(input("select a new location: "))
print(pathlib.Path.cwd())
