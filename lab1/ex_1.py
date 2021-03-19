# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:42:26 2021

@author: 11647
"""

"""
Exercise 1: Both Ends

Given a string s, return a string made of the first 2 and the last 2 chars of the original string

For example,

both_end('spring') should return 'spng'.

However, if the string length is less than 2, return the empty string.
"""

def both_ends(s):
    len_s = len(s)
    if len_s < 2:
        return ''
    else:
        return s[0:2]+s[-2:]
    
# answer
# def both_ends(s):
#     if len(s) < 2:
#         return ''
#     first2 = s[0:2]
#     last2 = s[-2:]
#     return first2 + last2 
                    
        
    # add your code here
aa = 'abcde'
# print(aa[-3:-1])
# print(aa[-2:])
print(both_ends('abcde'))