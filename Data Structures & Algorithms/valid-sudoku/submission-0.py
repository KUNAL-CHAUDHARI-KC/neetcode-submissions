class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate Rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item) 

        # validate cols
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item) 

        # validate Boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                s = set()

                for i in range(row, row+3):
                    for j in range(col, col+3):

                        item = board[i][j]

                        if item in s:
                            return False
                        elif item != '.':
                            s.add(item)
                
        return True




