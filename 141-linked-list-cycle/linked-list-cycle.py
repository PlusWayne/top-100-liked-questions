
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        pointer_1 = head
        pointer_2 = head
        while 1:
            try:
                pointer_1 = pointer_1.next
                pointer_2 = pointer_2.next.next
            except:
                return False
            if pointer_1 == pointer_2:
                return True
