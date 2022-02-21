class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        lens=len(nums)
        res=[]
        for i in range(lens):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=lens-1
            while (l<r):
                
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res
    
        
        
            
            
            
            
            
            
        