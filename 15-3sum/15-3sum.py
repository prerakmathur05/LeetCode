class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def twosum(nums,i,res):
            j=i+1
            hashmap={}
            while j<len(nums):
                target=-nums[i]-nums[j]
                if target in hashmap:
                    res.append([nums[i],target,nums[j]])
                    while j+1<len(nums) and nums[j]==nums[j+1]:
                        j+=1
                hashmap[nums[j]]=j
                j+=1
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i==0 or nums[i]!=nums[i-1]:
                twosum(nums,i,res)
        return res
                
        
        
        
            
            
        