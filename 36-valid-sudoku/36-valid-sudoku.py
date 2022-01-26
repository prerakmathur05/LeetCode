class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isrowvalid(row):
            rows=set()
            for i in board[row]:
                if i!=".":
                    if i in rows:
                        return False
                    else:
                        rows.add(i)
            return True
        def iscolvalid(col):
            cols=set()
            for j in range(9):
                if board[j][col]!=".":
                    if board[j][col] in cols:
                        return False
                    else:
                        cols.add(board[j][col])
            return True
        
        def issubmatrix(row):
            startr=row//3 *3
            for column in range(0,9,3):
                startc= column//3*3
                hashm=set()    
                for i in range(3):
                    for j in range(3):
                        if board[startr+i][startc+j]!=".":
                            if board[startr+i][startc+j] in hashm:
                                return False
                            else:
                                hashm.add(board[startr+i][startc+j])
            return True
        
        def isvalid(board):
            for row in range(9):
                if not isrowvalid(row):
                    return False
                if not iscolvalid(row):
                    return False
                if row % 3 ==0:
                    if not issubmatrix(row):
                        return False
            return True
        return isvalid(board)
                    
                    
           
        
        
                
            
            
                
            
        
                
    
        
        