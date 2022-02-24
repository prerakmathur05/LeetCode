# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        first=second=head
        dummy=ListNode(0)
        dummy.next=head
        first=second=dummy

        for i in range(n):
            first=first.next
        while first.next:
            first=first.next
            second=second.next
        second.next=second.next.next
        return dummy.next 
            
    
        
        
        
        '''
        size=0
        p=head
        while p:
            size+=1
            p=p.next
        if n>size:
            return -1
        pos=size-n
        curr=0
        p=head
        q=None
        while curr<pos:
            curr+=1
            q=p
            p=p.next
        if not q:
            return head.next
        q.next=p.next
        return head

        '''
        
            
        