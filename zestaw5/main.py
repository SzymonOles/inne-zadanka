import numpy as np
import math
import matplotlib.pyplot as plt
import random

RAN = 3000
LAM = 4
k = 0

# dane wylosowane
X = []
# prawdopodobienstwo teoretyczne
Y = []

q = np.exp(-LAM)
s = q
p = q

def poison(k,s,p):
    u = random.uniform(0,1)
    while u > s:
        k = k+1
        p = p * LAM / k
        s = s+p
    return k

def propability(LAM , k):
    return pow(LAM , k)/math.factorial(k) *np.exp(-LAM)

for x in range(RAN):
    X.append(poison(k,s,p))

for x in range(np.max(X)+1):
    Y.append(propability(LAM , x))

# ilosc elementow w kolumnach
Z = np.zeros(np.max(X)+1)

for x in range(np.size(X)):
    Z[X[x]]+= 1

# optymalizacja // biny szerokosci 1
for x in range(np.size(Z)):
    Z[x] = Z[x]/(RAN * 1)

ARR = np.arange(np.max(X)+1)
plt.plot(ARR, Y, '.-r', label = "oczekiwane") 
plt.plot(ARR, Z, '.-k', label = "wylosowane")
plt.legend()
plt.show()
