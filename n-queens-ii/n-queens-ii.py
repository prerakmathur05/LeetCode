class Solution:
    def totalNQueens(self, n: int) -> int:
        res=[]
        cols=set()
        rows=set()
        diagonals=set()
        antidiagonals=set()
        
        def placequeen(row,col):
            cols.add(col)
            diagonals.add(row-col)
            antidiagonals.add(row+col)
        
        def removequeen(row,col):
            cols.remove(col)
            diagonals.remove(row-col)
            antidiagonals.remove(row+col)
        
        def backtrack(row, cols, diagonals,antidiagonals,output):
            if row==n:
                res.append(output[:])
                return 1
            solutions=0
            for value in range(n):
                col=value
                diagonal = row-col
                antidiagonal=row+col
                if col not in cols and diagonal not in diagonals and antidiagonal not in antidiagonals:
                    placequeen(row,col)
                    output.append((row,col))
                    solutions+=backtrack(row+1,cols, diagonals,antidiagonals,output)
                    removequeen(row,col)
                    output.pop()
        
            
            return solutions
        
        sols= backtrack(0,cols,diagonals,antidiagonals,[])
        print(res)
        return sols
        
        