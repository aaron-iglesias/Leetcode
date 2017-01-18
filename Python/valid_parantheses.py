# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        st = []
        for c in s:
            if c == '(':
                st.append(')')
            elif c == '[':
                st.append(']')
            elif c == '{':
                st.append('}')
            elif len(st) == 0 or st.pop() != c:
                return False
        return len(st) == 0