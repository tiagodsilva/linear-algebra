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
print(eig_values, eig_vectors, sep='\n') 
inv_eig_vectors = np.linalg.inv(eig_vectors) 

alpha = inv_eig_vectors[0, 0] 
alpha_t_v = alpha * eig_vectors[:, 0] 

print(alpha_t_v * 18) 

for i in range(999): 
	x = m @ x 
print(x) 
