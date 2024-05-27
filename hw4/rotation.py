import numpy as np 
import scipy 

m = np.array([
	[2, -1, 2], 
	[2, 2, -1], 
	[-1, 2, 2] 
]) / 3 

# Compute m's eigenvalues 
evalues, evectors = np.linalg.eig(m) 
unit_eig_val = np.isclose(evalues.real, 1.) 
unit_eig_vec = evectors[:, unit_eig_val].reshape(-1, 1) 

print(unit_eig_vec) 

base, _ = np.linalg.qr(
	np.hstack([unit_eig_vec, np.eye(3)[1].reshape(-1, 1), np.eye(3)[2].reshape(-1, 1)]) 
) 

print(base) 

print(
	base.T @ m @ base  
) 

