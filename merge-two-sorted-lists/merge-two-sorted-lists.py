# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(p,q):
            if not q:
                return p
            elif not p:
                return q
            elif p.val<q.val:
                p.next=merge(p.next,q)
                return p
            else:
                q.next=merge(p,q.next)
                return q
        k=merge(list1,list2)
        return k 
        