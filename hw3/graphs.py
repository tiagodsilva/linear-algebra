import numpy as np 
import pandas as pd 
import scipy 
import networkx as nx 

def read_incd(): 
    incd = pd.read_csv('MatrizIncidencia.csv', sep=';', header=None).values 
    print(f'Read incidence matrix of shape {incd.shape}') 
    return incd 

def base_for_null_space(): 
    incd = read_incd()
    null_basis = scipy.linalg.null_space(incd) 
    null_basis = np.where(np.isclose(null_basis, 0.), 0., null_basis) 
    print(null_basis.shape) 
    pd.DataFrame(null_basis).to_csv(
            'null_basis.csv', index=None
        ) 
    
def conn_comp(): 
    incd = read_incd() 
    # Convert to an actual adjacency matrix 
    num_nodes = incd.shape[1] 
    amat = np.zeros((num_nodes, num_nodes)) 
    for node in range(num_nodes): 
        # Check edges starting at `node` 
        edges = incd[:, node] == 1
        # Find the corresponding vertices 
        incident_nodes = np.argwhere(incd[edges] == -1)
        amat[node, incident_nodes[:, 1]] = 1 
    graph = nx.from_numpy_array(amat) 
    cc = nx.connected_components(graph) 
    print(
            [(len(c), c) for c in cc ]
    ) 

    # Using the null-space
    P, L, U = scipy.linalg.lu(incd)  
    null_space_basis = scipy.linalg.null_space(incd) 
     
    for b in null_space_basis.T: 
        b = np.where(np.isclose(b, 0.), 0., b).astype('float16') 
        b_uni, indices, inverse = np.unique(b, return_index=True, return_inverse=True) 
        ccs = inverse 
        pd.DataFrame(ccs).to_csv(
                'connected_components.csv', index=None 
        ) 
    return amat 
        
if __name__ == '__main__': 
    # Exercise (a) 
    base_for_null_space() 
    # Exercise (b) 
    conn_comp() 
