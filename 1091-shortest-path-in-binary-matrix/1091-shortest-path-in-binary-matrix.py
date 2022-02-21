class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        maxrows=len(grid)-1
        maxcols=len(grid[0])-1
        directions=[(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
        if grid[0][0]==1 or grid[maxrows][maxcols]==1:
            return -1
        def neighbors(row,col):
            for r,c in directions:
                newrow=row+r
                newcol=col+c
                if not (0<=newrow<=maxrows and 0<=newcol<=maxcols):
                    continue
                if grid[newrow][newcol]!=0:
                    continue
                yield newrow,newcol
        grid[0][0]=1
        queue=deque([(0,0)])            
        while queue:
            r,c=queue.popleft()
            if (r==maxrows and c==maxcols):
                return grid[r][c]
            for row,col in neighbors(r,c):
                grid[row][col]=1 + grid[r][c]
                queue.append((row,col))
        return -1