# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        temp = head
        while temp and temp.next:
            total += 2
            temp = temp.next.next
        if temp:
            total += 1
        target = total - n - 1
        temp = head
        while temp and target:
            temp = temp.next
            target -= 1
        if temp and temp.next:
            temp.next = temp.next.next
        elif target <= 0:
            return head.next
        else:
            return
        return head
