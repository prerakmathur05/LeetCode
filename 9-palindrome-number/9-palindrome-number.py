class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        #we will reverse the number till half and then compare reverse with 1st half
        r=0
        while r<x:
            r=int(10*r+x%10)
            x/=10
            x=int(x)
            
        return r==x or x==int(r/10)
        
        
        
        
        def easy_method():
            num=str(x)
            r=len(num)-1
            l=0
            while l<r:
                if num[l]==num[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True

            