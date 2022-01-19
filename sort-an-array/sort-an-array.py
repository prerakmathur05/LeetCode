class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            l=len(nums)
            if l<=1:
                return nums
            mid=l//2
            left = mergesort(nums[:mid])
            right=mergesort(nums[mid:])
            return merge(left,right)
        def merge(left,right):
            l=r=0
            output=[]
            while l< len(left) and r<len(right):
                if left[l]<right[r]:
                    output.append(left[l])
                    l+=1
                else:
                    output.append(right[r])
                    r+=1
            output.extend(left[l:])
            output.extend(right[r:])
            return output
        return mergesort(nums)
                    