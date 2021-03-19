# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:49:57 2021

@author: 11647
"""

# Given a string s, return a string where all occurences of its first char have been changed to '*', except do not change the first char itself.

# For example

# fix_start('babble') should return 'ba**le'
# Assume that the string is length 1 or more.

# Hints: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.


def fix_start(s):
    firstChar = s[0]
    newStr = s[1:]
    return firstChar+newStr.replace(firstChar,'*')
 
# answer
# def fix_start(s):
#     front = s[0]
#     back = s[1:]
#     fixed_back = back.replace(front, '*')
#     return front + fixed_back

print(fix_start('abcaaa'))