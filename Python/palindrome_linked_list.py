# Given a singly linked list, determine if it is a palindrome.

class Solution(object):
    def isPalindrome(self, head):
        st = []
        tmp = head
        while tmp is not None:
            st.append(tmp.val)
            tmp = tmp.next
        while head is not None:
            if head.val != st.pop():
                return False
            head = head.next
        return True