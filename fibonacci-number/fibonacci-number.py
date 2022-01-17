class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n not in hashmap:
                hashmap[n]=f(n-1)+f(n-2)
            return hashmap[n]
        hashmap={}
        return f(n)
                
        