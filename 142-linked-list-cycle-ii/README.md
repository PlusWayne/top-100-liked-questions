# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        pointer_1 = head
        pointer_2 = head
        pointer_3 = head
        while 1:
            try:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next.next
            except:
                return None
            if pointer_1 == pointer_2:
                break
        while pointer_3 != pointer_1:
            pointer_1 = pointer_1.next
            pointer_3 = pointer_3.next
        return pointer_3
