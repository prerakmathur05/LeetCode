# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def minroot(root):
            if not root:
                return float("inf")
            mini=root.val
            mini=min(mini,minroot(root.left),minroot(root.right))
            return mini
        def maxroot(root):
            if not root:
                return float("-inf")
            maxi=root.val
            maxi=max(maxi,maxroot(root.left),maxroot(root.right))
            return maxi      
        
        def valid(root):
            if not root:
                return True
            if root.left and root.val<=maxroot(root.left):
                return False
            if root.right and root.val>=minroot(root.right):
                return False
            left = valid(root.left)
            right=valid(root.right)
            if left and right:
                return True
            else:
                return False
        return valid(root)