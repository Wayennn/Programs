import csv

class Subject:
    def __init__(self, name, units):
        self.name = name
        units = units.split("/")
        try:
            self.units = float(units[0])/float(units[1])
        except:
            self.units = float(units[0])

with open("Files\Subjects.csv", "r") as sfile:
    cread = csv.reader(sfile, delimiter = ",")
    subjs = [Subject(row[0], row[1]) for row in cread]

unitsum = 0
wgrsum = 0
for i in range(len(subjs)):
    unitsum += subjs[i].units
    wgrsum += float(input("Grade in " + subjs[i].name + ": "))*subjs[i].units
gwa = str(wgrsum/unitsum)
print("GWA is " + gwa)