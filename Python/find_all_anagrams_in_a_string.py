# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        d_p, d_s = {}, {}
        i = j = 0
        for c in p:
            d_p[c] = d_p[c] + 1 if c in d_p else 1
        for i in range(len(s)):
            if s[i] in d_p:
                d_s[s[i]] = d_s[s[i]] + 1 if s[i] in d_s else 1
                if i - j != len(p) - 1:
                    continue
            else:
                d_s = {}
                j = i + 1
                continue
            if d_p == d_s:
                res.append(j)
            d_s[s[j]] -= 1
            j += 1
        return res