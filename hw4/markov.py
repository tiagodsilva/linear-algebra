import numpy as np 

m = np.array([
	[.5, .3, .1],
	[.3, .4, .3], 
	[.2, .3, .6]  
]) 

x = np.array([0, 0, 1]).reshape(-1, 1) 
# x = np.array([.2, .4, .4]).reshape(-1, 1) 

print(
	m @ (m @ x) 
)

eig_values, eig_vectors = np.linalg.eig(m) 
inv_eig_vectors = np.linalg.inv(eig_vectors) 

# This operation is allowed since all elements in the first line of Q^{-1} are the same
alpha = inv_eig_vectors[0, 0]
alpha_t_v = alpha * eig_vectors[:, 0] 

stationary = lambda x: np.array([5/18, 1/3, 7/18]) * x.sum() 

for _ in range(12): 
	x = np.random.randn(3) 	
	print('analytic', stationary(x))
		
	for i in range(999): 
		x = m @ x 
	print('empirical', x) 
