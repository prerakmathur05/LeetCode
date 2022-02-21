class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        leng=len(nums)
        res=[]
        def twosum(nums,i,res):
            target=nums[i]
            r=leng
            hashmap={}
            j=i+1
            while j<r:
                t=-target-nums[j]
                if t in hashmap:
                    res.append([nums[i],t,nums[j]])
                    while j+1<r and nums[j]==nums[j+1]:
                        j+=1
                hashmap[nums[j]]=j
                j+=1
        for i in range(leng):
            if nums[i]>0:
                break
            if i==0 or nums[i-1]!=nums[i]:
                twosum(nums,i,res)
        return res
              
                
                
            
            
            
        