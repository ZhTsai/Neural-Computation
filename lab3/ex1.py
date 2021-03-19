# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:23:49 2021

@author: 11647
"""

"""
Exercise 1: tensordot

Given two tensors as follows:

a = np.random.randint(0,10,(4,4,5))
b = np.random.randint(0,10,(3,4,4))

Calculate the tensordot of the two tensors. How can we obtain a result tensor of shape (5, 3)?

"""

import numpy as np

## axes is int
A = np.array([[1,2],[1,2]])
B = np.array([[3,4],[3,4]])

C = np.tensordot(A, B, axes=([0,1]))

print(C.shape)
print(C)

# aa = np.random.randint(0,10,(2,1,2))
# bb = np.random.randint(0,10,(2,1,2))
# cc = np.tensordot(aa,bb)

# print(aa)