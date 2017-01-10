# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for c in s:
            d[c] = d[c] + 1 if c in d else 1
        for c in t:
            if c not in d or d[c] == 0:
                return False
            d[c] -= 1
        return True