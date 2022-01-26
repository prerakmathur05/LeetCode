# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res=[]
        def letstraverse(p):
            if p:
                res.append(p.val)
                letstraverse(p.left)
                letstraverse(p.right)
            else:
                return
        
        letstraverse(root1)
        letstraverse(root2)
        return sorted(res)
             
        