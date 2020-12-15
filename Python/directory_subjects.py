import os
import csv

with open("Files/G12Subjects.csv", "r") as sfile:
    sread = csv.reader(sfile, delimiter = ",")
    for i in sread:
        subjects = i

parent_path = "C:/Users/user/Documents/Grade 12/"
children_path = ["/Modules", "/Submissions"]

for i in range(len(subjects)):
    for j in range(len(children_path)):
        path = parent_path + subjects[i] + children_path[j]
        os.makedirs(path)
print("Directories Created")