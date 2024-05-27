import numpy as np 

m = np.array([
	[2/3, 1/3],
	[1/4, 3/4]
])

eig_values, eig_vectors = np.linalg.eig(m) 

print(eig_values * 12, eig_vectors, sep='\n') 

x = [2, 1] 

