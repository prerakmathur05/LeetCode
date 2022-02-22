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
​
return res
def two_sums_without_sort(nums):
dups=set()
res=set()
hashmap={}
for i in range(len(nums)):
if nums[i] not in dups:
dups.add(nums[i])
for j in range(i+1, len(nums)):
complement=-nums[i]-nums[j]
if complement in hashmap and hashmap[complement]==i:
res.add(tuple(sorted([nums[i],complement,nums[j]])))
hashmap[nums[j]]=i
return res