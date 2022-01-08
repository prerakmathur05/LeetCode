class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result=0
        curr=float("-inf")
        l=[]
        for value in nums:
            if value > curr:
                curr=value
                result+=curr
            else:
                l.append(result)
                curr=value
                result=value
                
        l.append(result)
        return max(l)
            
            
                
                
            
        
        