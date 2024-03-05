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
A, B, _ = load("CsBkg2")

yL = []

for i in range(len(B)):
    yL += [int(B[i] - A[i] * (2/3))]

y = abs(np.array(B) - (np.array(A) *2 /3))

xL = []
for i in range(1,1022):
    xL += [i]

x = np.array(xL)

max0 = [0,0]

for i in range(250,400):
    if y[i] > max0[0]:
        max0[0] = y[i]
        max0[1] = i

print(max0)



# Weighted fit.
#popt, pcov = curve_fit(f, x, y, p0, sigma=sig, absolute_sigma=True) 
#yfit = f(x, *popt)

#print('Weighted fit parameters:', popt)
#print('Covariance matrix:'); print(pcov)

#chi, p = sc.stats.chisquare(y,yfit)
#print("Chi: ",chi)
plt.plot(x,y)
#plt.errorbar(x, y, yerr=40, elinewidth=0.5, capsize = 2, c='0.5',lw=0) 

#plt.plot(x, yfit, label='Fit') 

#plt.xlabel("Time (s)")
#plt.ylabel("Amplitude (mV)")

#plt.ylim(-1000, 1000)
#plt.xlim(0,160)
#plt.legend(loc='lower center') 
plt.show()