# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def createTrees(start,end):
            if start>end:
                return [None,]
            all_trees=[]
            for i in range(start,end+1):
                #i is the root and we are creating left and right subtrees
                leftsubtrees=createTrees(start,i-1)
                rightsubtrees= createTrees(i+1,end)
                for l in leftsubtrees:
                    for r in rightsubtrees:
                        node=TreeNode(i)
                        node.left=l
                        node.right=r
                        all_trees.append(node)
            return all_trees
        return createTrees(1,n)
                        
                        
                        
                
                
                
            
            
            
            
            
        
        
        