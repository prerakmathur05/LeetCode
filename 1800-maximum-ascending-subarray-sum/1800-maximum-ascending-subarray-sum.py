class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result=0
        curr=float("-inf")
        maxi=0
        for value in nums:
            if value > curr:
                curr=value
                result+=curr
            else:
                maxi=max(maxi,result)
                curr=value
                result=value
                
        maxi=max(maxi,result)
        return maxi
            
            
                
                
            
        
        