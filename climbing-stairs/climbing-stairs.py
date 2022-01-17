class Solution:
    def climbStairs(self, n: int) -> int:
        def nways(k):
            if k==1:
                return 1
            if k==2:
                return 2
            if k not in hashmap:
                hashmap[k]=nways(k-1)+nways(k-2)
            return hashmap[k]
        hashmap={}
        return nways(n)