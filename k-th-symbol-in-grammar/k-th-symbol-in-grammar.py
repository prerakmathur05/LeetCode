import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def grammar(n,k):
            if n<0:
                return -1
            if n==1:
                return 0
            parent=grammar(n-1,math.ceil(k/2))  #k/2 + k%2 is math.ceil of k/2
            iskodd= (k%2==1)
            print(parent)
            if parent==1:
                return 1 if iskodd else 0
            else:
                return 0 if iskodd else 1
        return grammar(n,k)
            
        