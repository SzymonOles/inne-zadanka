import numpy as np
import matplotlib.pyplot as plt
import random


def A(x):
    return (np.sqrt(6 * x) - 1)

def B(x):
    return ((3 * x) - (1 / 2))

def C(x):
    return (3 - np.sqrt((-6 * x) + 6))

X = []

a=0
b=1/6
c=5/6
d=1

RAN = 100000

for x in range(RAN):
    r = random.uniform(0, 1)
    if r >= a and r< b:
        X.append(A(r))
    elif  r >= b and r< c:
        X.append(B(r))
    elif  r >= c and r< d:
        X.append(C(r))


plt.hist(X , bins=100 , density=1)
plt.show()