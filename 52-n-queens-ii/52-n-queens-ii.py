class Solution:
    def totalNQueens(self, n: int) -> int:
        if not n:
            return n
        def backtrack(row,diagonals,anti_diagonals,cols):
            if row==n:
                return 1
            solution=0
            for col in range(n):
                diagonal=row-col
                anti_diagonal=row+col
                if (col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals):
                    continue
                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)
                
                solution+=backtrack(row+1,diagonals,anti_diagonals,cols)
                # now backtrack by removing the queen from position
                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)
            return solution
        return backtrack(0,set(),set(),set())
        
        
        
        