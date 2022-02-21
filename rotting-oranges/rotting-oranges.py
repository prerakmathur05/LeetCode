class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges=0
        rowmax=len(grid)
        colmax=len(grid[0])
        rotten_oranges=[]
        for r in range(rowmax):
            for c in range(colmax):
                if grid[r][c]==1:
                        fresh_oranges+=1
                elif grid[r][c]==2:
                        rotten_oranges.append((r,c))
        queue=deque(rotten_oranges)
        if fresh_oranges==0:
            return 0
        
        def neighbor(row,col):
            directions=[(1,0),(0,-1),(-1,0),(0,1)]
            for u,v in directions:
                rnew,cnew=row+u,col+v
                if not (0<=rnew<rowmax and 0<=cnew<colmax):
                    continue
                if grid[rnew][cnew]!=1:
                    continue
                yield rnew,cnew
        
        time=0
        while queue:
            temp=[]
            for _ in range(len(queue)):
                row,col=queue.popleft()
                for rnew,cnew in neighbor(row,col):
                    grid[rnew][cnew]=2
                    fresh_oranges-=1
                    temp.append((rnew,cnew))
            time+=1
            queue.extend(temp)
            print(queue)
        
        return time-1 if fresh_oranges ==0 else -1            
                    
                
            


        