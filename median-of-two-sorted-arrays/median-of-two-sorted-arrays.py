class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(B)< len(A):
            A,B= B,A
        l=0
        r=len(A)-1
        total_length=len(A)+len(B)
        half = total_length//2
        while 1:
            mid=(l+r)//2
            j= half-mid-2
            Aleft=A[mid] if mid>=0 else float("-inf")
            Bleft= B[j] if j>=0 else float("-inf")
            Aright = A[mid+1] if mid+1<len(A) else float("inf")
            Bright= B[j+1] if j+1 <len(B) else float("inf")
            
            if Aleft<=Bright and Bleft<=Aright:
                #odd
                if total_length%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r=mid-1
            else:
                l=mid+1
                
        