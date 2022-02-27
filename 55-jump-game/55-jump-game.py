class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        @lru_cache(maxsize=None)
        def dp(i):
            if i==n-1:
                return True
            if nums[i]==0:
                return False
            farjump=min(n-1-i,nums[i])
            for j in range(farjump,0,-1):
                c=dp(i+j)
                if c:
                    return True
            return False
        return dp(0)

