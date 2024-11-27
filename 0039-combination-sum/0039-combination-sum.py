class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtracking(result, num, idx):
            if num == target:
                answer.append(result)
                return
            
            if num > target:
                return

            for i in range(idx, len(candidates)):
                backtracking(result + [candidates[i]], num + candidates[i], i)

        backtracking([], 0, 0)
        return answer

        