# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=pointer=ListNode(0)
        carry=0
        p=l1
        q=l2
        while p or q:
            x=p.val if p else 0
            y=q.val if q else 0
            sums=x+y+carry
            if sums >= 10:
                carry=1
            else:
                carry=0
            t=ListNode(sums%10)
            pointer.next=t
            pointer=t
            p=p.next if p else None
            q=q.next if q else None
        if carry >0:
            t=ListNode(carry)
            pointer.next=t
            poinetr=t
        return head.next
        
        
            
        
            
            
                
            
        