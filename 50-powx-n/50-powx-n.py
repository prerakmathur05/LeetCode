class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastpow(x,n):
            if n==0:
                return 1
            halfpower= fastpow(x,n//2)
            if n%2==0:
                return halfpower*halfpower
            else:
                return halfpower*halfpower * x
        if n<0:
            x=1/x
            n=-1* n
        return fastpow(x,n)
        
                
        