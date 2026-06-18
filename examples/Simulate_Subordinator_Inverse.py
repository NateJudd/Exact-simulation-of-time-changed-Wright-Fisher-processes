#this is the example of OU process, for more detail, see Section 4.2 
import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy.special import gamma, beta, expit, logit, logsumexp, erf
from scipy.special import eval_jacobi, gammaln,  polygamma, exp1, erfinv
from scipy.stats import expon, multivariate_normal
from scipy import special
from scipy import stats
from matplotlib import rc
import seaborn as sns
import pandas as pd

import source

random.seed(2023) # not working?

alpha=0.5
alpha1 = 0.5
alpha2 =  0.9
theta1 = 1 / (-gamma(-alpha1))
theta2 = 1 / (-gamma(-alpha2))
q = 1.0
r = 1
mass = 1/2 # 1/2
Lambda1 = 2.20171  # \int_0^1 (1-e^(-qx))x^(-alpha-1)dx
Lambda2 = 1.66667  # \int_1^infty x^(-alpha-1)dx
randmass = Lambda1+Lambda2

def my_rand():
    if np.random.rand() < Lambda1 / (Lambda1 + Lambda2):
        X = np.random.rand()**(1 / (1 - alpha))
        while np.random.rand() > (1 - np.exp(-q * X)) / (q * X):
            X = np.random.rand()**(1 / (1 - alpha))
    else:
        X = np.random.rand()**(-1 / alpha)
    return X
t1 = 0.25
t2 = 0.5
t3 = 1
t4 = 2

n = int(1e3)
y1 = np.zeros(n); y2 = np.zeros(n)
y4 = np.zeros(n);  y3 = np.zeros(n)
#xarr = np.arange(0, 4.05, 0.05)
#yarr = np.arange(0, 4.05, 0.05)
#T = np.zeros(n)
#U = np.zeros(n)

#u = np.zeros((len(xarr), len(yarr)))
#gmma = np.array([[1, 1], [0, 1]])  # gmma is the volatility of the SDE


def myrand_lambda():  # Q has levy density 1{s>1}s^(-5)
    return np.power(np.random.rand(), -1 / 4)

for i in range(n):
    auxT, auxU, auxV = source.rand_crossing_subordinator(alpha1, theta1, q, t1, 0, 1, mass, Lambda1+Lambda2, my_rand); y1[i]= auxT
    auxT, auxU, auxV = source.rand_crossing_subordinator(alpha1, theta1, q, t2, 0, 1, mass, Lambda1+Lambda2, my_rand); y2[i]= auxT
    auxT, auxU, auxV = source.rand_crossing_subordinator(alpha1, theta1, q, t3, 0, 1, mass, Lambda1+Lambda2, my_rand); y3[i]= auxT
    auxT, auxU, auxV = source.rand_crossing_subordinator(alpha1, theta1, q, t4, 0, 1, mass, Lambda1+Lambda2, my_rand); y4[i]= auxT

#    auxT, auxU, auxV = source.rand_crossing_subordinator(alpha2, theta2, q, t, 0, 1, mass, randmass, #myrand_lambda); y2[i]= auxT


# Combine into a DataFrame
df = pd.DataFrame({'y1': y1, 'y2': y2, 'y4': y4, 'y3': y3})

# Save as CSV
filename = f"subordinator_alpha{alpha1}_randmass{randmass}.csv"

# Save as CSV
df.to_csv(filename, index=False)


x = np.arange(1, len(y1) + 1)


plt.figure(figsize=(6,4))
sns.kdeplot(y1, label='t=0.25', color='royalblue', linewidth=2)
sns.kdeplot(y2, label='t=0.5', color='yellow', linewidth=2)
sns.kdeplot(y3, label='t=1', color='orange', linewidth=2)
sns.kdeplot(y4, label='t=2', color='red', linewidth=2)


plt.xlabel('Value')
plt.ylabel('Density')
mytitle = f"Density estimates of {r}-truncated tempered {alpha1}-stable\n subordinator with compound Poisson process"
plt.title(mytitle)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
