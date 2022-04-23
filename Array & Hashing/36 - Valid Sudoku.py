class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Time: O(n^2), where n = 9
        Space: O(n^2)
        '''
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        sqset = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                sqrow, sqcol = r // 3, c // 3
                sqpos = sqrow * 3 + sqcol
                if board[r][c] in rowset[r] or board[r][c] in colset[c] or board[r][c] in sqset[sqpos]:
                    return False
                rowset[r].add(board[r][c])
                colset[c].add(board[r][c])
                sqset[sqpos].add(board[r][c])
        return True
