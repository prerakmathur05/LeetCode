class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rowmax=len(heights)
        colmax=len(heights[0])
        grid=[[float("inf")]* colmax for i in range(rowmax)]
        grid[0][0]=0
        
        visited=[[False]*colmax for i in range(rowmax)]
        print(visited)
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        def neighbor(row,col):
            for x,y in directions:
                newrow= row+x
                newcol=col+y
                if not (0<=newrow<rowmax and 0<=newcol<colmax):
                    continue
                yield newrow, newcol
        heap=[(0,0,0)]
        while(heap):
            diff,row,col=heapq.heappop(heap)
            visited[row][col]=True
            for newrow,newcol in neighbor(row,col):
                if not visited[newrow][newcol]:
                    currentdiff=abs(heights[newrow][newcol]-heights[row][col])
                    maxdiff=max(currentdiff, grid[row][col])
                    if maxdiff < grid[newrow][newcol]:
                        grid[newrow][newcol]=maxdiff
                        heapq.heappush(heap,(maxdiff,newrow,newcol))
                        
                        
                
            
            
        return grid[-1][-1]
                

        
        
        
        