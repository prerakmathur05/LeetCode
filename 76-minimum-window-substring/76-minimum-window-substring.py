class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {i:t.count(i) for i in t}
        have = {i:0 for i in t}
        haveV, needV= 0,len(need)
        res,reslen=[-1,-1], float("inf")
        l=0
        for r in range(len(s)):
            c=s[r]
            have[c]=1+have.get(c,0)
            if c in t and need[c]==have[c]:
                haveV+=1
            while(needV==haveV):
                if reslen > r-l+1:
                    reslen=r-l+1
                    res=[l,r]
                have[s[l]]-=1
                if s[l] in t and have[s[l]]< need[s[l]]:
                    haveV-=1
                
                l+=1
        l,r=res
        return s[l:r+1] if reslen!= float("inf") else ""    
        
#         l=len(s)
#         o=len(t)
#         i=j=0
#         initlimit=maxlimit=0
#         while(1):
#             if t not in s[i:j]:
#                 j+=1
#             else:
#                 maxlimit=j
#                 i+=1
#                 if t not in s[i:maxlimit]:
#                     initlimit=i-1
#                     break
#         return s[initlimit:maxlimit]
    
            
#         @lru_cache(maxsize=None)
#         def dp(i):
#             if i==l:
#                 return s
#             if s[i] not in t:
#                 return dp(i+1)
#             case1=s[i]
#             for j in range(i+1,l):
#                 case1+=s[j]
#                 h=0
#                 for k in t:
#                     if k in case1:
#                         h+=1
#                     else:
#                         break
#                 if h==o-1:
#                     break
#             case2=dp(i+1)
#             print(case1)
#             print(case2)
#             l1=len(case1)
#             l2=len(case2)
#             return case1 if l1<l2 else case2
#         return dp(0)
                
        