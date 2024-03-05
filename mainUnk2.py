# eg8-curve-fit.py
import numpy as np
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt
import scipy as sc
import statistics
from load import load
import math as m

M0, tau = 100, 47
A = M0
A, B, _ = load("Unk2Bkg")

xL = []
for i in range(1,1022):
    xL += [i]

y = abs(np.array(B) - (np.array(A) *2 /3))
x = np.array(xL)


# Main Max Calc
max0 = [0,0]
for i in range(2,1000):
    if y[i] > max0[0]:
        max0[0] = y[i]
        max0[1] = i

print(max0)

#Secondary Max
max1 = [0,0]
for i in range(60,1000):
    if y[i] > max1[0]:
        max1[0] = y[i]
        max1[1] = i

print(max1)

#Third Max
max2 = [0,0]
for i in range(121,1000):
    if y[i] > max2[0]:
        max2[0] = y[i]
        max2[1] = i

print(max2)

#Fourth Max
max3 = [0,0]
for i in range(184,1000):
    if y[i] > max3[0]:
        max3[0] = y[i]
        max3[1] = i

print(max3)

#Fifth Max
max4 = [0,0]
for i in range(290,1000):
    if y[i] > max4[0]:
        max4[0] = y[i]
        max4[1] = i

print(max4)

#E Converter
mCon = 2.5458
bCon = -.7272

E1 = max0[1] * mCon + bCon
E2 = max1[1] * mCon + bCon
E3 = max2[1] * mCon + bCon
E4 = max3[1] * mCon + bCon
E5 = max4[1] * mCon + bCon

print("Main Max:",E1)
print("Secodary Max:",E2)
print("Third Max:",E3)
print("Fourth Max:",E4)
print("Fifth Max:",E5)

plt.plot(x,y)
plt.show()