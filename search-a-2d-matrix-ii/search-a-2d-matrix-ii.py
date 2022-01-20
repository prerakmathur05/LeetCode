import sys
sys.setrecursionlimit(20000)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        def findin(target,left,up,right,down):
            if left>right or up>down:
                return False
            if target> matrix[down][right] or target<matrix[up][left]:
                return False
            mid_col=left + (right-left)//2
            row=up
            for i in range(up+1,down+1):
                if matrix[i][mid_col]<=target:
                    row+=1
            if matrix[row][mid_col]==target:
                return True
            r1=findin(target,mid_col+1,up,right,row)
            r2=findin(target,left,row,mid_col-1,down)
            return r1 or r2
        return findin(target,0,0,len(matrix[0])-1,len(matrix)-1)
        