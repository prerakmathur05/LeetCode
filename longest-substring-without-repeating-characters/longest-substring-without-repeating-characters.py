class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        curr=0
        dic=set()
        l=0
        for r in range(len(s)):
            if s[r] not in dic:
                dic.add(s[r])
                curr+=1                
            else:
                res=max(res,curr)
                curr=1
                dic=set()
                dic.add(s[r])
                i=r-1
                while s[i] not in dic and i>=0:
                    curr+=1
                    dic.add(s[i])
                    i-=1
        res=max(res,curr)
        return res
                
        
        
        
        