# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution(object):
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            # odd number of letters in palindrome
            j = k = i
            while j - 1 >= 0 and k + 1 < len(s) and s[j - 1] == s[k + 1]:
                j -= 1
                k += 1
            if k - j + 1 > len(res):
                res = s[j:k+1]
            # even number of letters in palindrome
            j, k = i, i + 1
            if k == len(s) or s[j] != s[k]:
                continue
            while j - 1 >= 0 and k + 1 < len(s) and s[j - 1] == s[k + 1]:
                j -= 1
                k += 1
            if k - j + 1 > len(res):
                res = s[j:k+1]
        return res