#!/usr/bin/env python3

cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D
import numpy as np 

def cat_matrices2D(mat1, mat2, axis=0):
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        new_mat=np.concatenate((mat1,mat2),axis=0)
        return new_mat.tolist()
    elif (len(mat1) == len(mat2)) and axis == 1:
        new_mat=np.concatenate((mat1,mat2),axis=1)
        return new_mat.tolist()
    else:
        return None
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
print(mat4)
print(mat5)
mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)
print(mat4)
print(mat5)