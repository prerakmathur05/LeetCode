class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(array):
            k=len(array)
            if k:
                if k%2!=0:
                    return array[(k-1)//2]
                else:
                    return (array[k//2] + array[(k-2)//2])/2
            else:
                return None
            
        array=nums1+nums2
        array.sort()
        return median(array)