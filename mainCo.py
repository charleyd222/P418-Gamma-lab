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
A, B, _ = load("CoBkg2")

#A: Bkg
#B: Co Data by bin

yL = []

for i in range(len(B)):
    yL += [int(B[i] - A[i])]

y = abs(np.array(B) - (np.array(A)))

xL = [] #bin numbers
for i in range(1,1022): #Creates bin #'s
    xL += [i]

x = np.array(xL) 

#Find Mins
min1 = [1000000000000,0]
min2 = [1000000000000,0]

for i in range(390,430):
    if B[i] < min1[0]:
        min1 = [B[i],i]

print(min1)
for i in range(551,570):
    if B[i] < min2[0]:
        min2 = [B[i],i]

print(min2)

min1[0] = 168
min1[1] = 417

xFit = np.array(xL)

# Slope Calc, (y1 - y0) / (x1 - x0)
m = (min2[0]-min1[0])/(min2[1]-min1[1])
print(m)


xFitL = []
yFitL = []

#min1[1] -> x0
#min1[0] -> y0

#Find 2 peaks +- 2 bins



def f(x): #Linear Fit
    return  m * x - m * min1[1] + min1[0]

for i in range(min1[1],553):
    yFitL += [f(xL[i])]
    xFitL += [i]

xFit = np.array(xFitL)
yFit = np.array(yFitL)

yProsL = []
xProsL = []

for i in range(len(yFitL)):
    yProsL += [yL[xFitL[i]] - yFitL[i]]
    xProsL += [xFitL[i]]


yPros = np.array(yProsL)
xPros = np.array(xProsL)


#Peak 1
i0 = 430
max0 = [0,0]
for i in range(80):
    if yProsL[i] > max0[0]:
        max0[0] = yProsL[i]
        max0[1] = i+i0

#Peak 2

max1 = [0,0]
for j in range(40):
    if yProsL[i+j] > max1[0]:
        max1[0] = yProsL[i+j]
        max1[1] = j+i+i0

print(max0,max1)
y0 = max0[1]
#dX = 2
#dY = ??




# Weighted fit.
#popt, pcov = curve_fit(f, x, y, p0, sigma=sig, absolute_sigma=True) 
#yfit = f(x, *popt)

#print('Weighted fit parameters:', popt)
#print('Covariance matrix:'); print(pcov)

#chi, p = sc.stats.chisquare(y,yfit)
#print("Chi: ",chi)
plt.plot(x,y)
plt.plot(xFit,yFit)
plt.plot(xPros,yPros)
#plt.errorbar(x, y, yerr=40, elinewidth=0.5, capsize = 2, c='0.5',lw=0) 

#plt.plot(x, yfit, label='Fit') 

#plt.xlabel("Time (s)")
#plt.ylabel("Amplitude (mV)")

#plt.ylim(-1000, 1000)
#plt.xlim(0,160)
#plt.legend(loc='lower center') 
plt.show()