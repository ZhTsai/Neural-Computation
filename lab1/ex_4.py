# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:27:51 2021

@author: 11647
"""

"""
Given a list of numbers, return a list where adjacent identical elements 
are replaced by a single element.

For example,

[1,2,2,3] yields [1,2,3]
[1,1,1,2,3,4,4,5] yields [1,2,3,4,5]
You may create a new list or modify the passed in list.
"""

def remove_adjacent(nums): 
    new_list = nums[0:1]
    for i in nums:
        if i != new_list[-1]:
            new_list.append(i)
    
    return new_list

# correct answer
# def remove_adjacent(nums):
#     result = []
#     for num in nums:
#         if len(result) == 0 or num != result[-1]:
#             result.append(num)
#     return result


l = [1,4,4,3,3,2,1,1,5]

print(remove_adjacent(l))