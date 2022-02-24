class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>=1:
                nums[abs(nums[i])-1]*=-1         
            else:
                continue
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
        
        
        
            
            