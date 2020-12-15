class Dog:
    def __init__(self, h = 0, t = 0, s = 0, n = "askal"):
        self.hunger = h
        self.thirst = t
        self.sadness = s
        self.name = n
    def timepast(self):
        self.hunger += 1
        self.thirst += 1
        self.sadness += 1

butter = Dog(13, 92, 47, "Butter")
tabby = Dog(11, 1, 100, "Tabby")
odie = Dog(0, 0, 0, "Odie")
doglist = [butter, tabby, odie]
for j in doglist:
    for i in range(0, 10):
        print(j.name + "'s hunger: " + str(j.hunger) + " points.")
        print(j.name + "'s thirst: " + str(j.thirst) + " points.")
        print(j.name + "'s sadness: " + str(j.sadness) + " points.")
        j.timepast()