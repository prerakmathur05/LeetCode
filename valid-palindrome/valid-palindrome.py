class Solution:
    def isPalindrome(self, s: str) -> bool:
        def ispalindrome(s,left,right):
            if left<right:
                if s[left]!=s[right]:
                    return False
                r=ispalindrome(s,left+1,right-1)
                if not r:
                    return False
                else:
                    return True
            else:
                return True
        
        def preparestring(s):
            r=""
            for i in range(len(s)):
                if s[i].isalnum():
                    r+=s[i].lower()
            return r
        test= preparestring(s)
        return ispalindrome(test,0,len(test)-1)
        
            
