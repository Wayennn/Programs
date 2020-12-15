a = 1
b = 1
for i in range(100000000):
    #print(b)
    c = a
    a = b + a
    b = c
print(a)