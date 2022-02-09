class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(2000)
        def dp(i):
            if i==0:
                return nums[i]
            if i==1:
                return max(nums[1],nums[0])
            return max(dp(i-1), nums[i]+dp(i-2))
        return dp(len(nums)-1)
        