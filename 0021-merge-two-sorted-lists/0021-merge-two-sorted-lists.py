# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Head = None
        head1 = list1
        head2 = list2
        if not head1:
            return head2
        if not head2:
            return head1
        dummy = ListNode()
        current = dummy
        while(head1 and head2):
            if head1.val <= head2.val:
                current.next = head1
                current = current.next
                head1 = head1.next
            else:
                current.next = head2
                current = current.next
                head2 = head2.next
        if head2:
            current.next = head2
        if head1:
            current.next = head1
        return dummy.next