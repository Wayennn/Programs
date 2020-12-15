import math
import random

def check(n):
    if n==1:
        return "Nither prime nor composite"
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return "Composite"
        return "Prime"
        
x = random.randint(100, 1000)
print("The number " + str(x) + " is " + check(x))