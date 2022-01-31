class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(2000)
        def dp(i):
            if i==0:
                return cost[0]
            if i==1:
                return cost[1]
            return cost[i] + min(dp(i-2), dp(i-1))
        return min(dp(len(cost)-1),dp(len(cost)-2))
                