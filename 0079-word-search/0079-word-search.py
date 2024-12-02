class Solution:
    # 15 글자
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def backtracking(idx, curi, curj):

            if idx == len(word):
                return True
                

            if curi < 0 or curi >= rows or curj < 0 or curj >= cols:
                return False
            if board[curi][curj] != word[idx] or visited[curi][curj]:
                return False


            visited[curi][curj] = True

            di = [1, -1, 0, 0]
            dj = [0, 0, 1, -1]

            for k in range(4):
                newi, newj = curi + di[k], curj + dj[k]
                if backtracking(idx + 1, newi, newj):
                    return True

            visited[curi][curj] = False

            return False

        for i in range(rows):
            for j in range(cols):
                if backtracking(0, i, j):
                    return True

        return False