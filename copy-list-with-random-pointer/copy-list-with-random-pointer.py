"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited={}
        def copyLL(head):
            if not head:
                return head
            if head in visited:
                return visited[head]
            newnode=Node(head.val)
            visited[head]=newnode
            newnode.next=copyLL(head.next)
            newnode.random=copyLL(head.random)
            return newnode
        newnode=copyLL(head)
        return newnode
        
        
        