import numpy as np
'''

1 2  | -6 5         1 2 -6 -5
3 4  | -4 3   -->   3 4 -4 -3
5 6  | -2 1         5 6 -2 -1

[[1, 2, -6, -5], 
[3, 4, -4, -3], 
[5, 6, -2, -1]]
'''

a=np.array([[-6, 5], [-4, 3], [-2, 1]])
b=np.array([[1, 2], [3, 4], [5, 6]])
c = np.concatenate((b,a),axis=1)
print(c)