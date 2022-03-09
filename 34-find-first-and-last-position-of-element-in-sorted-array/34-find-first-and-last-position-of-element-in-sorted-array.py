class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bst(nums, target,isfirst):
            start=0
            end=len(nums)-1
            while start<=end:
                mid= (start+end)//2
                if nums[mid]==target:
                    if isfirst:
                        if mid==start or nums[mid-1]<target:
                            return mid
                        end=mid-1
                    else:
                        if end==mid or nums[mid+1]>target:
                            return mid
                        else:
                            start=mid+1
                elif nums[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            return -1
        start1= bst(nums, target, True)
        if start1==-1:
            return [-1,-1]
        end1= bst(nums, target, False)
        return [start1,end1]
        
                
        
        
        
        
        '''
        start=-1
        end=-1
        for i,num in enumerate(nums):
            if num == target:
                if start==-1:
                    start=i
                else:
                    end=i
        if start!=-1 and end==-1:
            end=start
        return [start,end] 
        '''
        