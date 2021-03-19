# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:44:59 2021

@author: 11647
"""

# Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order.

# You may modify the passed in lists.

def linear_merge(list1, list2):
    list3 = list1 + list2
    len_list3 = len(list3)
    times = len_list3
    for t in range(times):
         for i in range(len_list3-1):
             if list3[i]>list3[i+1]:
                temp = list3[i]
                list3[i] = list3[i+1]
                list3[i+1] = temp
         len_list3 -= 1

    # add your code here
    return list3

# correct answer
# def linear_merge(list1, list2):
#     result = []
    
#     # Look at the two lists so long as both are non-empty.
#     # Take whichever element [0] is smaller.
#     while len(list1) and len(list2):
#         if list1[0] < list2[0]:
#             result.append(list1.pop(0))
#         else:
#           result.append(list2.pop(0))

#     # Now tack on what's left
#     result.extend(list1)
#     result.extend(list2)
#     return result

l1 = [1,4,7,9]
l2 = [2,5,6,8]
# l1.extend(l2)
# print(l1)
print(linear_merge(l1,l2))