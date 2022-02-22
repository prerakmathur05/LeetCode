class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        leng=len(nums)
        res=[]
        
    
        def two_sum_without_hashmap(nums,i,res):
            l=i+1
            r=leng-1
            while l<r:
                target=nums[i]+nums[l]+nums[r]
                if target>0:
                    r-=1
                elif target<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    
        def two_sum_with_hashmap(nums,i,res):
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
                 #two_sum_with_hashmap(nums,i,res)
                two_sum_without_hashmap(nums,i,res)

        return res
              
        
    def two_sums_without_sort(nums):
            l=len(nums)
            hashmap={}
            result=()
            duplicates=set()
            for i in range(l):
                if nums[i] not in duplicates:
                    for j in range(i+1,l):
                        target=-nums[i]-nums[j]
                        if target in hashmap and hashmap[target]==i:
                                                                        result.add(tuple(sorted([nums[i],target,nums[j]])))
                        hashmap[nums[j]]=i

        
                        
                
            
            
            
        