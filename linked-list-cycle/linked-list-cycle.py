# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p=q=head
        while p and q:
            p=p.next
            if p:
                p=p.next
                if p==q:
                    return True
            q=q.next
        return False
            
        