class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for value in num:
            while stack and stack[-1]>value and k:
                stack.pop()
                k-=1
            stack.append(value)
        
        finalstack=stack[:-k] if k else stack
        return "".join(finalstack).lstrip('0') or '0'
              
            
        
        
        