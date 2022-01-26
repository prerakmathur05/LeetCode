class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(2000)
        def dp(i):
            if i==0:
                return 0
            if i==1:
                return 1
            if i==2:
                return 1
            return dp(i-1)+dp(i-2)+dp(i-3)
        return dp(n)