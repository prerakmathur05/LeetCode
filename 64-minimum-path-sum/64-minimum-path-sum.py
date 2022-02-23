class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        Seems to be a DP problem at first but if we closely observe, the               allowed movement is right and down only, so it can be solved with             greedy too
        '''
        rowmax=len(grid)
        colmax=len(grid[0])
        matrix=[[0 for i in range(colmax)] for i in range(rowmax)]
        matrix[0][0] = grid[0][0]
        for i in range(1,rowmax):
            matrix[i][0]=matrix[i-1][0]+grid[i][0]
        for i in range(1,colmax):
            matrix[0][i]=matrix[0][i-1]+grid[0][i]
        for row in range(1,rowmax):
            for col in range(1,colmax):
                matrix[row][col]=grid[row][col]+min(matrix[row-1][col],matrix[row][col-1])
        return matrix[rowmax-1][colmax-1]
    
            
        
        