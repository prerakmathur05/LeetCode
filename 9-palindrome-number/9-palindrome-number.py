class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        def ispalin(s,left,right):
            if left>=right:
                return True
            if s[left]!=s[right]:
                return False
            rec=ispalin(s,left+1,right-1)
            return True if rec else False
        
        return ispalin(num,0,len(num)-1)
        
        