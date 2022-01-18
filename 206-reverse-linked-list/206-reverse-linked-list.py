# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if not head or not head.next:
                return head
            p = reverse(head.next)
            head.next.next=head
            head.next=None
            return p
        return reverse(head)
        
        
#         r,q=None,None
#         p=head
#         while(p):
#             r=q
#             q=p
#             p=p.next
#             q.next=r
#         head=q
#         return head
        