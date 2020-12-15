import csv

class Drug:
    def __init__(self, hprodid, hprodname, genname, gencode):
        self.hprodid = hprodid
        self.hprodname = hprodname
        self.genname = genname
        self.gencode = gencode

with open("Files\edpms_druglist.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        print(",".join(row))