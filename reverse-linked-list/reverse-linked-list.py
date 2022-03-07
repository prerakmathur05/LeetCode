# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reversing(head):
            if not head or not head.next:
                return head
            #next_node=ListNode(0)
            next_node=reversing(head.next)
            head.next.next=head
            head.next=None
            return next_node
        
        return reversing(head)
        '''
        
        q=r=None
        p=head
        while p:
            r=q
            q=p
            p=p.next
            q.next=r
        return q
        
        '''
        