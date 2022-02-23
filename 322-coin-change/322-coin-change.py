class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Since it is asking for optimal solution and my current decision is             dependent on previous decision it's the question of our favourite             concept Dynamic Programming ;)
        '''
        @lru_cache(maxsize=None)
        def dp(r):
            if r<0:
                return -1
            elif r==0:
                return 0
            mincount=float('inf')
            for coin in coins:
                count=dp(r-coin)
                if count==-1:
                    continue
                mincount=min(mincount,count+1)
            if mincount==float("inf"):
                return -1
            else:
                return mincount
        return dp(amount)
        
        
        