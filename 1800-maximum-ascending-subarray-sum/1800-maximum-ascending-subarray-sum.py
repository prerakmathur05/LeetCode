class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        #WE will  use Kadane's Algorithm for this problem
        curr=-1
        result=nums[0]
        final_result=0
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                result+=nums[i+1]
            else:
                final_result=max(final_result,result)
                result=nums[i+1]       
        final_result=max(final_result,result)
        return final_result
            
            
                
                
            
        
        