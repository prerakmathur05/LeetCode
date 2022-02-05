# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None        
        queue=deque([root])
        result=[]

        while queue:
            nodesatsamelevel=[]
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr:
                    nodesatsamelevel.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if nodesatsamelevel:
                result.append(nodesatsamelevel)
        return result
        

        