class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        s=[]
        def backtrack(s,left,right): #s is list
            if len(s)==2*n:
                sr="".join(s)
                result.append(sr)
                return 
            if left<n:
                s.append("(")
                backtrack(s,left+1,right)
                s.pop()
            if right<left:
                s.append(")")
                backtrack(s,left,right+1)
                s.pop()
        
        backtrack(s,0,0)
        return result
        
        
        
        
        def catalan(n):
            if n==0:
                return 1
            if n==1:
                return 1
            res=0
            for i in range(n):
                res+=catalan(n-i-1)*catalan(i)
            return res
        return catalan(n)