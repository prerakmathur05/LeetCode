class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,start):
            i=start
            n=len(nums)
            j=n-1
            while(i<j):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
                
        l=len(nums)
        i=l-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
        j=l-1
        
        if i>=0:

            while(j>i and nums[j]<=nums[i]):
                j-=1

            nums[i],nums[j]=nums[j],nums[i]
        reverse(nums,i+1)

        
# below code won't work because operations like sort and sorted are not allowed
#         l=len(nums)
#         flag=0
#         u=0
#         for i in range(l-2,-1,-1):
#             if nums[i]<nums[i+1]:
#                 flag=1
#                 if i==0:
#                     target=i+1
#                     u=1
#                     for j in range(1,l):
#                         if nums[j]>nums[i]:
#                             target=j
#                         else:
#                             break
#                     #nums=nums[target:]+nums[:target]
#                     first=nums[target]
#                     nums.pop(target)
#                     nums = [first] + sorted(nums)
                    
#                     print(nums)
#                 else:
#                     print("esdsfs")
#                     nums[i],nums[i+1]=nums[i+1],nums[i]
#                 break
#         if flag==0:
#             print("runs")
#             nums=sorted(nums)
        