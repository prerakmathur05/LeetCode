# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import ctypes
#ctypes.cast(address, ctypes.py_object).value
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        p=root
        output=[]
        while p or st:
            if p:
                st.append(id(p))
                p=p.left
            else:
                temp=st.pop()
                if temp>0:
                    st.append(-temp)
                    p=ctypes.cast(temp,ctypes.py_object).value
                    p=p.right
                else:
                    temp=abs(temp)
                    temp=ctypes.cast(temp,ctypes.py_object).value
                    output.append(temp.val)
                    p=None
        return output
        