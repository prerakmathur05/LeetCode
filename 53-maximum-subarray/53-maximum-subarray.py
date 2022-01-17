class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we will use kadane's algorithm
        curr=float("-inf")
        result=float("-inf")
        for num in nums:
            curr=max(curr+num,num)
            result=max(result,curr)
        return result
        
        