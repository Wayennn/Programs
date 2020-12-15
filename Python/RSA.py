import random

primes = [999863, 999883, 999907, 999917, 999931, 999953, 999959, 999961, 999979, 999983]
primes1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
primes2 = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]
primes3 = list()

with open("Files\primes-1k-to-10k.txt", "r") as fl:
    for line in fl.readlines():
        primes3.append(int(line))
l = int(len(primes3))-1

check = False
while check==False:
    p = primes3[random.randint(0, l)]
    q = primes3[random.randint(0, l)]
    if (p-1)%3!=0 and (q-1)%3!=0 and p!=q:
        check = True
n = p*q
d = int((2*(p-1)*(q-1)+1)/3)

print("Public Key: " + str(n))
print("Secret Key: " + str(d))

k = int(input("Key (<" + str(n) + "): "))
print("K = " + str(k))
c = (k**3)%n
print("C = " + str(c))

f = (c**d)%n
print("Recovered K = " + str(f))