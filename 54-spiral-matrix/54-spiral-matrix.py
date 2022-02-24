class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowmax=len(matrix)
        colmax=len(matrix[0])
        res=[]
        def spiral(row,col,rowmax,colmax):
            if row>=rowmax or col>=colmax:
                return
            
            for i in range(col,colmax):
                res.append(matrix[row][i])
            for i in range(row+1,rowmax):
                res.append(matrix[i][colmax-1])
            if row!=rowmax-1: 
                for i in range(colmax-2,col-1,-1):
                    res.append(matrix[rowmax-1][i])
            if col!=colmax-1:
                for i in range(rowmax-2,row,-1):
                    res.append(matrix[i][col])
            spiral(row+1,col+1,rowmax-1,colmax-1)
        
        spiral(0,0,rowmax,colmax)

        return res

            
        


                
                
            
                
            
            
            
            
            
        
        