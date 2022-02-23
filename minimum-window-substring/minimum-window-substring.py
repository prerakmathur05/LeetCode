class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dict={i:t.count(i) for i in t}
        req_len=len(target_dict)
        curr_dict={}
        cur_len=0
        l=0
        r=len(s)
        res=''
        res_len=float('inf')
        for i in range(len(s)):
            c=s[i]
            curr_dict[c]=curr_dict.get(c,0)+1
            if c in t and curr_dict[c]==target_dict[c]:
                cur_len+=1
                while cur_len==req_len:
                    curr=i-l+1
                    if res_len>curr:
                        res_len = curr
                        res=s[l:i+1]
                    curr_dict[s[l]]-=1
                    if s[l] in t and curr_dict[s[l]]<target_dict[s[l]]:
                        cur_len-=1
                    l+=1
        return res
                            
                        
                    
                        
                        