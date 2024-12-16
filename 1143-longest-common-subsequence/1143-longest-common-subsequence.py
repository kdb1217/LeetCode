class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) >= len(text2):
            big = text1
            small = text2
        else:
            big = text2
            small = text1

        dpTable = [([0] * (len(big) + 1)) for _ in range(len(small) + 1)]
        answer = -1

        for i in range(len(small)):
            for j in range(len(big)):
                if small[i] == big[j]:
                    print(small[i], big[j])
                    dpTable[i][j] = dpTable[i - 1][j - 1] + 1
                else:
                    dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])
                answer = max(answer, dpTable[i][j])

        return answer

