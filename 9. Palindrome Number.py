'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        integer=str(x)
        if integer[0]=="-":
            return False
        elif integer[0::]==integer[::-1]:
            return True 
        else: 
            return False
    

