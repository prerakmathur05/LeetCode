class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        end=len(nums)
        def threesum(i,nums,res):
            j=i+1
            while j<end:
                l=j+1
                r=end-1
                while l<r:
                    #[-5,-5,-4,-4-2,-2,0,0] -13
                    g_value=nums[i]+nums[j]+nums[l]+nums[r]
                    diff = g_value-target
                    if diff<0:
                        l+=1
                    elif diff>0:
                        r-=1
                    else:
                        res.add(tuple([nums[i],nums[j],nums[l],nums[r]]))
                        l+=1
                        r-=1
                        # while l+1<r and nums[l]==nums[l+1]:
                        #     l+=1
                        # while j+1<end and nums[j]==nums[j+1]:
                        #     j+=1
                j+=1
        for i in range(end):
            threesum(i,nums,res)
        return res
            
        
        