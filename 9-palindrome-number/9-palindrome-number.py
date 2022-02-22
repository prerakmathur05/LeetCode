class Solution:
    def isPalindrome(self, x: int) -> bool:
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
        
            