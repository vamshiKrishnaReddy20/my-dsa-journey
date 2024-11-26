# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        if head is not None:
            nxt = head.next
        else:
            return head
        while(nxt):
            current.next = prev
            prev = current
            current = nxt
            nxt = nxt.next
        current.next = prev
        return current