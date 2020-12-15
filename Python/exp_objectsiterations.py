import csv

class myClass:
    def __init__(self, subs = [], skip = 1):
        self.subs = subs
        self._index = -skip
        self.skip = skip
    def __iter__(self):
        return self
    def __next__(self):
        if self._index<(len(self.subs)-self.skip):
            self._index += self.skip
            return self.subs[self._index]
        else:
            raise StopIteration

with open("Files\Subjects.csv", "r") as sfile:
    cread = csv.reader(sfile, delimiter = ",")
    subjs = [row[0] for row in cread]

obj = myClass(subjs, 1)

for i in obj:
    print(i)