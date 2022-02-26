class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #here input array is already sorted
        n=len(nums)
        i=0
        j=n-1
        result=[0]*(n)
        for r in range(n-1,-1,-1):
            if abs(nums[i])>abs(nums[j]):
                      square=nums[i]
                      i+=1
            else:
                      square=nums[j]
                      j-=1
            result[r]=square*square
                      
                      

        return result
        
                
                
            
        
        
        
        
        
        
        
#         squares=[n**2 for n in nums]
#         radix=[0]*(max(squares)+1)
        
#         for num in squares:
#             radix[num]+=1
#         final=[]
#         for i,value in enumerate(radix):
#             if value==0:
#                 continue
#             else:
#                 c=value
#                 while c>0:
#                     final.append(i)
#                     c-=1
#         return final
                    
        