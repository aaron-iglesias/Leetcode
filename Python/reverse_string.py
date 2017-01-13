# Write a function that takes a string as input and returns the string reversed.

class Solution(object):
    def reverseString(self, s):
        s_list = list(s)
        s_list.reverse()
        return ''.join(s_list)