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
                box = {}

                for row in range(rows, rows+3):
                    for col in range(cols, cols+3):
                        if board[row][col] == ".":
                            continue
                        
                        if board[row][col] in box:
                            return False
                        else:
                            box[board[row][col]] = 1

                        

        return True
        

        