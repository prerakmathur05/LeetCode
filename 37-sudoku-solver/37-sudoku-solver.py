class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=defaultdict(list)
        cols=defaultdict(list)
        
        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    rows[r].append(board[r][c])
                    cols[c].append(board[r][c])
        
        def placevalue(value,row,col):
            board[row][col]=value
            rows[row].append(value)
            cols[col].append(value)
            
        def removevalue(value,row,col):
            rows[row].remove(value)
            cols[col].remove(value)
            board[row][col]="."
        
        def isvalidinsubmatrix(value,row,col):
            startindexrow= row//3 *3
            startindexcol=col//3 * 3
            for i in range(3):
                for j in range(3):
                    if value == board[startindexrow+i][startindexcol+j]:
                        return False
            return True
        issolved = False
        def backtrack(row,col):
            print(row)
            if row==9:
                nonlocal issolved
                issolved = True
                return      
        #    print(f"{row}, {col}")
            if board[row][col]==".":
                for value in range(1,10):
                    value=str(value)
                    if value in rows[row] or value in cols[col] or not isvalidinsubmatrix(value,row,col):
                        continue
                    else:
                        placevalue(value,row,col)
                        if col==8:
                            backtrack(row+1,0)
                        else:
                            backtrack(row,col+1)
                        if not issolved:
                            removevalue(value,row,col)

            else:
                if col==8:
                    backtrack(row+1,0)
                else:
                    backtrack(row,col+1)
        
        return backtrack(0,0)
            
            