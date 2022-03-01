class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        @lru_cache(2000)
        def dp(i, h):
            if i==l:
                return 0
            if h:
                return max(prices[i]+dp(i+1,0),dp(i+1,1))
            else:
                return max(-prices[i]+dp(i+1,1), dp(i+1,0))
        return dp(0,0)    
        