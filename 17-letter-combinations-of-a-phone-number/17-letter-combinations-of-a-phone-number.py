class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)<1:
            return None
        graph={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        n=len(digits)
        res=[]
        def backtrack(i,output):
            if len(output)==n:
                res.append("".join(output))
                return
            
            for alphabets in graph[digits[i]]:
                output.append(alphabets)
                backtrack(i+1,output)
                output.pop()
        backtrack(0,[])
        return res
                 
                
                
                
        