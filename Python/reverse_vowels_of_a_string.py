# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            tmp = s_list[i]
            s_list[i] = s_list[j]
            s_list[j] = tmp
            i += 1
            j -= 1
        return ''.join(s_list)