class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums= sum(nums)
        if sums%2!=0:
            return False
        n=len(nums)
        @lru_cache(maxsize=None)
        def dp(i,r):
            if r<0:
                return False
            elif r==0:
                return True
            if i==n:
                return False
           
            return dp(i+1,r-nums[i]) or dp(i+1,r) 
        return dp(0,sums//2)
        
        
        
        
        
        
        
        
        
        