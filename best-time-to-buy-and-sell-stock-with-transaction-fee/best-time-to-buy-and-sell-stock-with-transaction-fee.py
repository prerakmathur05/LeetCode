class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(2000)
        def dp(i,h):
            if i==len(prices):
                return 0
            if h:
                sell=prices[i]+dp(i+1,0)-fee
                notsell= dp(i+1,1)
                return max(sell,notsell)            
            else:
                buy=-prices[i]+dp(i+1,1)
                notbuy= dp(i+1,0)
                return max(buy,notbuy)
        return dp(0,0)
                
        