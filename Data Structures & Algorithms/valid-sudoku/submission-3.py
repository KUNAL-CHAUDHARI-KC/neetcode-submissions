class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for i in range(len(board)):
            rows = {}
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue 

                if board[i][j] in rows:
                     return False
                
                else:
                    rows[board[i][j]] = 1
                     
        
        for j in range(len(board[0])):
            cols = {}
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue 

                if board[i][j] in cols:
                     return False
                
                else:
                    cols[board[i][j]] = 1

        for rows in range(0, 9, 3):
            for cols in range(0, 9, 3):
                boxes ={}

                for r in range(rows, rows+3):
                    for c in range(cols, cols+3):


                        if board[r][c] == ".":
                            continue 
                        
                        if board[r][c] in boxes:
                            return False
                        
                        else:
                            boxes[board[r][c]] = 1
        
        return True

            


        
                     

        
        