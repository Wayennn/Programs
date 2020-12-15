primes = list()
with open("Files\primes-to-1000k.txt", "r") as fl:
    for line in fl.readlines():
        primes.append(int(line))
for i in range(0, len(primes)-1):
    print(primes[i])
