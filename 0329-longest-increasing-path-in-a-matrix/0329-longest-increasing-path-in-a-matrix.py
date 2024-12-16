class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]


        def backtracking(i, j):
            nonlocal answer
            if dp[i][j] != -1:
                return dp[i][j]
            
            di = [1, -1, 0, 0]
            dj = [0, 0, 1, -1]
            max_value = 1

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] < matrix[i][j]:
                    max_value = max(max_value, 1 + backtracking(ni, nj))

            dp[i][j] = max_value
            return dp[i][j]

        answer = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                answer = max(answer, backtracking(i, j))

        print(answer)
        return answer

            




