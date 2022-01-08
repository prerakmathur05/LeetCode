class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        #WE will  use Kadane's Algorithm for this problem
        curr=-1
        result=final_result=0
        for value in nums:
            if value > curr:
                curr=value
                result+=curr
            else:
                final_result=max(final_result,result)
                curr=value
                result=value       
        final_result=max(final_result,result)
        return final_result
            
            
                
                
            
        
        