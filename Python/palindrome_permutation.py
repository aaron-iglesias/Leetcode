# Given a string, determine if a permutation of the string could form a palindrome.

# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.

class Solution(object):
    def canPermutePalindrome(self, s):
        hash_set = set()
        for c in s:
            if c in hash_set:
                hash_set.remove(c)
            else:
                hash_set.add(c)
        return len(hash_set) <= 1