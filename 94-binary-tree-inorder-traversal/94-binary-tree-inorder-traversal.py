# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        if not root:
            return []
        stack=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            l.append(curr.val)
            curr=curr.right
        return l
        
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        return l
        