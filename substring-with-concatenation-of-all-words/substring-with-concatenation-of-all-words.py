class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lw=len(words[0])
        end=len(s)
        l=0
        target_dict={word:words.count(word) for word in words}
        have_dict={word:0 for word in words}
        req_count=len(target_dict)
        res=[]
        while l<end:
            r=l
            count=0
            have_dict={word:0 for word in words}
            while r<end:
                c=s[r:r+lw]
                if c in target_dict:
                    have_dict[c]+=1
                    if have_dict[c]==target_dict[c]:
                        count+=1
                    elif have_dict[c]>target_dict[c]:
                        break
                    if count==req_count:
                        res.append(l)
                    r+=lw
                else:
                    break
            l+=1
        return res
                    
                    
                        
            
            
            
        