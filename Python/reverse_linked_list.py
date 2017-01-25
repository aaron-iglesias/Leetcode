# reverse singly linked list

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        tmp = head
        st = []
        while tmp is not None:
            st.append(tmp.val)
            tmp = tmp.next
        tmp = head
        while tmp is not None:
            tmp.val = st.pop()
            tmp = tmp.next
        return head