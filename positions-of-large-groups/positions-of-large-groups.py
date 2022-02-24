class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        rarray=[]
        l=0
        r=len(s)
        count=0
        res=""
        while l<r:
            j=1
            res+=s[l]
            while l+j<r and s[l+j]==s[l]:
                res+=s[l+j]
                j+=1
            if len(res)>=3:
                rarray.append((l,l+j-1))
                res=""
            else:
                res=""
            l+=j
        return rarray
            
                

                
            
            
        