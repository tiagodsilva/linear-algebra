import numpy as np 
import matplotlib.pyplot as plt 
import sys
sys.path.append('.') 
from mpl_preamble import * 

if __name__ == '__main__': 
    p = np.array(
            [[0, 1], [1, 0], [2, -1], [3, 2]] 
        ) 
    x, y = p[:, 0], p[:, 1] 
    m = np.vstack(
            [np.ones_like(x), x, x ** 2, x ** 3]
        ) 
    a = np.linalg.inv(m.T) @ y 
    
    x_range = np.linspace(x.min() - .5, x.max() + .5, 128) 
    x_power = np.vstack(
            [np.ones_like(x_range), x_range, x_range ** 2, x_range ** 3]
    ) 
    y_power = a @ x_power
    
    plt.plot(x_range, y_power, zorder=0)
    plt.scatter(x, y, color='tomato') 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.savefig('pol.pdf', bbox_inches='tight') 
