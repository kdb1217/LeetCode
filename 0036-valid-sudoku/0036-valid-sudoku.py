class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 * 9 보드가 9개이며 9개의 보드가 모두 스도쿠 규칙이 맞는지 확인하는 문제?
        nums = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for i,j in nums:
            y, x = i, j
            boardchecker = set()
            for i in range(y, y + 3):
                for j in range(x, x + 3):
                    if board[i][j].isdigit():
                        if board[i][j] in boardchecker:
                            return False
                        else:
                            boardchecker.add(board[i][j])

        for i in range(9):
            horizonChecker = set()
            verticalChecker = set()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in horizonChecker:
                        return False
                    else:
                        horizonChecker.add(board[i][j])
                
                if board[j][i].isdigit():
                    if board[j][i] in verticalChecker:
                        return False
                    else:
                        verticalChecker.add(board[j][i])
        return True



    