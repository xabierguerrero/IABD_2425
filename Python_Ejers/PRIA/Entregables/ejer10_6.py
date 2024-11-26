import numpy as np

nums=np.array([-3, -2, -1, 0, 1, 2, 3])
arr2D_1=np.random.choice(nums, size = (3, 4))
arr2D_2=np.random.choice(nums, size = (3, 4))
print(arr2D_1)
print("                +")
print(arr2D_2)
print("-----------------")
print(arr2D_1+arr2D_2)