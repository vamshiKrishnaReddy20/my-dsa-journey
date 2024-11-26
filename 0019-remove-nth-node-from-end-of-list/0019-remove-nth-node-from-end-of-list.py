# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fst = head
        prev = dummy
        for _ in range(n):
            fst = fst.next
        while fst:
            prev = prev.next
            fst = fst.next
        prev.next = prev.next.next
        return dummy.next           
