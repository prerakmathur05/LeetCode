class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
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
        