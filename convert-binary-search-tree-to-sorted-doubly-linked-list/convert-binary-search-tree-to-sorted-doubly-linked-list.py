"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #inorder traversal of bst will result in sorted list
        if not root:
            return root
        tree=[]
        def inorder(root):
            if root:
                inorder(root.left)
                tree.append(root.val)
                inorder(root.right)
        
        inorder(root)
        print(tree)
        first=last=Node(tree[0])
        
        for i in range(1,len(tree)):
            t=Node(tree[i])
            t.left=last
            last=t
    
        last.right=first
        first.left=last
        t=last.left
        for i in range(1,len(tree)):
            t.right=last
            last=t
            t=t.left
            print(t.val)
        return first
            