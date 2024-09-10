import numpy as np

def matrix_power( A, m):
    
    A= np.array(A)
   
    if A.shape[0] != A.shape[1]:
        raise ValueError("The input matrix must be square")
    
    
    res = np.linalg.matrix_power(A, m)
    
    return res


A = [[1, 2], 
     [3, 4]]
m = 2
res = matrix_power(A, m)
print("A^m is:\n", res)
