# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:55:09 2021

@author: 11647
"""

"""
Given a list of strings, return a list with the strings in sorted order, 
except group all the strings that begin with 'x' first.

For example,

['mix','xyz','apple','xanadu','aardvark'] yields ['xanadu','xyz','aardvark','apple','mix'].
Hint: this can be done by making two lists and sorting each of them before combining them.
"""

def front_x(words):
    x_list = []
    nor_list = []
    for string in words:
        if string[0] == 'x':
            x_list.append(string)
        else:
            nor_list.append(string)


    return sorted(x_list) + sorted(nor_list)

# correct answer
# def front_x(words):
#     x_list = []
#     other_list = []
#     for w in words:
#         if w.startswith('x'):
#             x_list.append(w)
#         else:
#             other_list.append(w)
#     return sorted(x_list) + sorted(other_list)


ll = ['abc','aaa','aba','xab','xza','xzzz','xzz']
print(front_x(ll))