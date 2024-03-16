import numpy as np 

def elementar_matrix(i, j, n=4, m=4): 
    m = np.zeros((n, m)) 
    m[i, j] = 1 
    return m 

if __name__ == '__main__': 
    np.random.seed(42) 
    B = np.random.rand(4, 4) 
    B_clone = B.copy() 
    I = np.eye(4) 

    left_matrix = np.eye(4) 
    right_matrix = np.eye(4) 
    print(B) 
    print('+' * 32) 
    B = B @ (I + elementar_matrix(0, 0)) # a 
    right_matrix = right_matrix @ (I + elementar_matrix(0, 0)) 
    print(B) 
    print('+' * 32) 
    B = (I - 2/3 * elementar_matrix(0, 0)) @ B # b   
    left_matrix = (I - 2/3 * elementar_matrix(0, 0)) @ left_matrix 
    print(B) 
    print('+' * 32) 
    B = (I + elementar_matrix(0, 2)) @ B # c 
    left_matrix = (I + elementar_matrix(0, 2)) @ left_matrix 
    print(B) 
    print('+' * 32) 
    B = B @ (I \
         - elementar_matrix(0, 0) + elementar_matrix(0, 3) \
            - elementar_matrix(3, 3) + elementar_matrix(3, 0) 
    ) # d 
    right_matrix = right_matrix @ (I \
         - elementar_matrix(0, 0) + elementar_matrix(0, 3) \
            - elementar_matrix(3, 3) + elementar_matrix(3, 0) 
    ) 
    print(B) 
    print('+' * 32) 
    B = (I - elementar_matrix(0, 1) - \
         elementar_matrix(2, 1) - elementar_matrix(3, 1)) @ B # e 
    left_matrix = (I - elementar_matrix(0, 1) - \
         elementar_matrix(2, 1) - elementar_matrix(3, 1)) @ left_matrix 
    print(B) 
    print('+' * 32) 
    B = B @ (I - elementar_matrix(3, 3) + elementar_matrix(2, 3)) # f
    right_matrix = right_matrix @ (I - elementar_matrix(3, 3) + elementar_matrix(2, 3))  
    print(B) 
    print('+' * 32) 
    B = B @ I[:, 1:] 
    right_matrix = right_matrix @ I[:, 1:]  
    print(B) 
    print('+' * 32) 

    print(left_matrix, right_matrix) 
    print(left_matrix @ B_clone @ right_matrix) 
    