class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(2000)
        def catalan(n):
            if n==0:
                return 1
            elif n==1:
                return 1
            
            k=0
            for i in range(n):
                k+=catalan(i)*catalan(n-i-1)
            return k
        return catalan(n)