import numpy as np 
import sys
import time 
import tqdm 
sys.path.append('.') 
from mpl_preamble import * 

TRIALS = 200 

if __name__ == '__main__':
    sizes = 2 ** (4 + np.arange(8)) 
    runtimes = np.zeros((len(sizes), TRIALS)) 
    for idx, size in enumerate(sizes): 
        for trial in tqdm.trange(TRIALS): 
            m = np.random.randn(size, size) 
            y = np.random.randn(size) 
            s = time.time() 
            a = np.linalg.solve(m, y) 
            runtimes[idx, trial] = time.time() - s 
    avg = np.log(runtimes).mean(axis=1) 
    std = np.log(runtimes).std(axis=1) 
    log_sizes = np.log(sizes) 
    linreg, _, _, _ = np.linalg.lstsq(log_sizes.reshape(-1, 1), avg.reshape(-1, 1))
    print(linreg.squeeze()) 
    plt.plot(log_sizes, avg) 
    plt.fill_between(log_sizes, avg-std, avg+std, alpha=.5) 
    plt.xlabel('Tamanho da matriz (log)') 
    plt.ylabel('Tempo de execução (log)')  
    plt.savefig('hw1/figures/runtimes.pdf', bbox_inches='tight') 