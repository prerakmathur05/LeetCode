class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bst(nums,left,right):
            if left>=right:
                return right
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return bst(nums,left,mid)
            else:
                return bst(nums,mid+1,right)
        return bst(nums,0,len(nums))