# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=ListNode(0)
        def swap(head):
            if not head or not head.next:
                return head
            fnode=head
            snode=head.next
            fnode.next=swap(snode.next)
            snode.next=fnode
            return snode
            
                             
        return swap(head)
            
            
           