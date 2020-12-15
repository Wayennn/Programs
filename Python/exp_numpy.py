import numpy as np
from numpy import random

lst = [random.randint(100, size=(2, 7)) for i in range(3)]
array = np.array(lst)
print(array)
print(type(array))

n = np.arange(50)
print(n)
print(type(n))