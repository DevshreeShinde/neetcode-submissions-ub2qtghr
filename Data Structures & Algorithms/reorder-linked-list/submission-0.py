# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        #slow is at middle now reverse second half
        prev=None
        curr=slow.next
        slow.next=None
        while curr:
           nextnode=curr.next
           curr.next=prev
           prev=curr
           curr=nextnode
        first=head
        second=prev
        while second:
            tmp1=first.next
            tmp2=second.next
            second.next=first.next
            first.next=second
            first=tmp1
            second=tmp2
        
        