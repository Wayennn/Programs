n = int(input("Public key (N): "))
while True:
    k = int(input("Key (integer that is <" + str(n) + "): "))
    if k<n:
        break
    print("You can only enter a key that is an integer <" + str(n))
print("K = " + str(k))
c = (k**3)%n
print("C = " + str(c))