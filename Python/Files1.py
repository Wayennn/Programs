def datlen(d):
    i = 0
    for j in d:
        i += 1
    return i

dat = dict({"Name":"", "Age":"", "Gender":"", "Campus":""})

while True:
    for i in dat:
        dat[i] = input("Enter " + i + ": ")
        
    with open("Files\Data.txt") as fl:
        lines = fl.readlines()
        try:
            e = int(lines[-(2+datlen(dat))])
        except IndexError:
            e = 0

    with open("Files\Data.txt", "a") as fl:
        fl.write("Entry number\n" + str(e+1) + "\n")
        for i, j in dat.items():
            fl.write(i + ": " + j + "\n")
        fl.write("\n")
    c = input("One more entry (y/n)? ")
    if c.lower()!="y":
        break