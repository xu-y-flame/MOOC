# coding=utf-8
'''
Created on 2015年11月2日

@author: xuyan
'''
import numpy as np

# list of row lists
print [[0 for j in range(4)] for i in range(3)]
print [[i-j for j in range(4)] for i in range(3)]
print

mat1 = np.mat([[1, 2, 3], [3, 3, 5]])
mat1_T = np.mat([[1, 2, 3], [3, 3, 5]]).transpose()
print mat1, type(mat1)
print mat1_T
print mat1 * mat1_T
print  

arr1 = np.array([[1, 2, 3], [3, 3, 5]])
print arr1, type(arr1)

set1 = {(i-j) for j in range(4) for i in range(3)}

print type(set1), set1