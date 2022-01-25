class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        res=[]
        def backtrack(output, value, k):
            if k==0:
                res.append([output[:]])
                return 
            else:
                for i in range(n+1):
                    output.append(i)
           
        '''         
        res=[]
        curr=[]
        def backtrack(num,curr):
            if len(curr)==k:
                res.append(curr[:])
            else:
                for i in range(num,n+1):
                    curr.append(i)
                    backtrack(i+1,curr)
                    curr.pop()
        
        backtrack(1,curr)
        return res