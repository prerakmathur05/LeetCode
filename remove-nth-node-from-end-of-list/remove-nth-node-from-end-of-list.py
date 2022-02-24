# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        p=head
        while p:
            size+=1
            p=p.next
        if n>size:
            return -1
        pos=size-n+1
        curr=0
        p=head
        q=None
        while curr<pos-1:
            curr+=1
            q=p
            p=p.next
        if not q:
            return head.next
        q.next=p.next
        return head
            
            
        