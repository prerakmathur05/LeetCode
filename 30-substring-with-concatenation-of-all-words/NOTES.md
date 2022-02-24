<--------Below is the original code---->
```
lw=len(words[0])
end=len(s)
l=0
target_dict={word:words.count(word) for word in words}
have_dict={word:0 for word in words}
print(target_dict)
count=0
req_count=len(target_dict)
res=[]
while l<end:
if s[l:l+lw] in target_dict:
have_dict[s[l:l+lw]]+=1
if have_dict[s[l:l+lw]]==target_dict[s[l:l+lw]]:
count+=1
elif have_dict[s[l:l+lw]]>target_dict[s[l:l+lw]]:
have_dict={word:0 for word in words}
have_dict[s[l:l+lw]]=1
count=0
if have_dict[s[l:l+lw]]==target_dict[s[l:l+lw]]:
count+=1
if count==req_count:
initial_index=l+lw-(req_count*lw)
res.append(initial_index)
have_dict={word:0 for word in words}