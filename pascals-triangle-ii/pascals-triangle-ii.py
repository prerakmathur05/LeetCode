class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @lru_cache(20000)
        def pascal(r,c):
            if c==0 or c==r:
                return 1
            return pascal(r-1,c-1)+ pascal(r-1,c)
        output=[]
        for i in range(rowIndex+1):
            output.append(pascal(rowIndex,i))
        return output
            
        
        