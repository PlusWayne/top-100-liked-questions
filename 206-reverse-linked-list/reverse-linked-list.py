# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head
        prev, cur, nex = None, head, head.next
        cur.next = prev
        while nex != None:
            prev, cur, nex = cur, nex, nex.next
            cur.next = prev
        return cur
