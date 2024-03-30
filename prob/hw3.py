import numpy as np 
import matplotlib.pyplot as plt 
import sys
sys.path.append('..') 
from mpl_preamble import * 

def f1(x): 
    match x: 
        case _ if x < 0: 
            return 0 
        case _ if 0 <= x <= 500: 
            return 5 / 6 * (x / 1000) 
        case _ if 500 < x <= 1000: 
            return (x - 500) / 1000 * 1 / 6 + 5 / 6 * (x / 1000) 
        case _ if 1000 < x <= 1500: 
            return (x - 500) / 1000 * 1 / 6 + 5 / 6 
        case _ if x > 1500: 
            return 1 

def f2(x): 
    match x: 
        case _ if x < 0: 
            return 0 
        case _ if x <= 0: 
            return 1 / 6 
        case _ if 0 < x < 1000: 
            return 1 / 6 + 4 / 6 * (x / 1000) 
        case _ if x <= 1000: 
            return 2 / 6 + 4 / 6 * (x / 1000) 
        case _ if x > 1000: 
            return 1 

plt.figure(figsize=(6, 3)) 

plt.subplot(1, 2, 1) 
xs = np.linspace(-100, 1600, num=400) 
ys = [f1(x) for x in xs]
plt.plot(xs, ys, zorder=0) 
plt.scatter(
        [500, 1000, 1500], [f1(500), f1(1000), f1(1500)], color='orange'
)
plt.xlabel('$x$') 
plt.ylabel('$F_{a}(x)$') 
plt.xlim(-100, 1600) 

plt.subplot(1, 2, 2) 

xs = np.linspace(-100, 0, num=50, endpoint=False) 
print(xs) 
ys = [f2(x) for x in xs]
plt.plot(xs, ys, zorder=0, color='blue') 

xs = np.linspace(0, 1000, num=200, endpoint=False) 
ys = [f2(x) for x in xs] 
plt.plot(xs, ys, zorder=0, color='blue') 

xs = np.linspace(1000, 1100, num=50, endpoint=False) 
ys = [f2(x) for x in xs] 
plt.plot(xs, ys, zorder=0, color='blue') 

plt.scatter(
        [0, 1000], [f2(0), f2(1000)], color='orange'
)

plt.xlabel('$x$') 
plt.ylabel('$F_{b}(x)$') 
plt.xlim(-100, 1100) 

plt.tight_layout() 

plt.savefig('hw3.pdf') 

# plt.show() 

xs = np.linspace(0., 1., num=700) 
cdf = xs ** 2 
pdf = 2 * xs 

plt.clf() 

plt.subplot(1, 2, 1) 
plt.plot(xs, cdf) 
plt.title('$F_{Z}$') 
plt.xlabel('$z$') 
plt.subplot(1, 2, 2) 
plt.plot(xs, pdf) 
plt.title('$f_{Z}$') 
plt.xlabel('$z$') 
plt.savefig('hw3_uniform.pdf', bbox_inches='tight') 
plt.show() 
