# beware before executing

import os
import random

parent_path = "C:/Users/user/Documents/random/"
i = 0
while i<100:
    directory = str(random.randint(1, 100)) + "/"
    path = parent_path + directory
    try:
        os.makedirs(path)
        print("Directory " + path + " created.")
        i += 1
    except FileExistsError:
        print("Directory " + path + " already exists.")
        continue
    with open(path + "File number " + str(i+1) + ".txt", "x") as fl:
        f = fl.write("bzzt")
