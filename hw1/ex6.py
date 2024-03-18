import torch # as np 
import sys
import time 
import tqdm 
sys.path.append('.') 
from mpl_preamble import * 

TRIALS = 200 
device = 'cuda' if torch.cuda.is_available() else 'cpu' 

if __name__ == '__main__':
    sizes = 2 ** (4 + torch.arange(8, device=device)) 
    runtimes = torch.zeros((len(sizes), TRIALS), device=device) 
    for idx, size in enumerate(sizes): 
        for trial in tqdm.trange(TRIALS): 
            m = torch.randn((size, size), device=device) 
            y = torch.randn((size,), device=device) 
            s = time.time() 
            torch.linalg.solve(m, y) 
            runtimes[idx, trial] = time.time() - s 
    avg = torch.log(runtimes).mean(axis=1).cpu().numpy()
    std = torch.log(runtimes).std(axis=1).cpu().numpy() 
    log_sizes = torch.log(sizes).cpu().numpy() 
    linreg, _, _, _ = np.linalg.lstsq(log_sizes.reshape(-1, 1), avg.reshape(-1, 1))
    print(linreg.squeeze()) 
    plt.plot(log_sizes, avg) 
    plt.fill_between(log_sizes, avg-std, avg+std, alpha=.5) 
    plt.xlabel('Tamanho da matriz (log)') 
    plt.ylabel('Tempo de execução (log)')  
    plt.savefig('hw1/figures/runtimes.pdf', bbox_inches='tight') 
