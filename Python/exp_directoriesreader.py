# reader of exp_directories.py

import os

parent_path = "C:/Users/user/Documents/random/"

for i in range(1, 101):
    try:
        file_name = str((os.listdir(parent_path + str(i)))[0])
        path = parent_path + str(i) + "/" + file_name
        with open(path) as fl:
            print("File from " + path + " says " + fl.read())
    except FileNotFoundError:
        try:
            print("Oops! File from " + path + " not found.")
        except NameError:
            print("Oops! Directory from " + parent_path + " not found.")
