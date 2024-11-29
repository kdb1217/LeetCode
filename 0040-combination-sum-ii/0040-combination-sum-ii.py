class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        visited = [False] * len(candidates)

        def backtracking(arr, sumArr, idx):
            if sumArr == target:
                answer.append(arr)
                return

            if sumArr > target:
                return

            for i in range(idx, len(candidates)):
                if not visited[i]:
                    visited[i] = True
                    if i > 0 and candidates[i] == candidates[i - 1] and not visited[i - 1] and candidates[i] <= target:
                        visited[i] = False
                        continue
                    backtracking(arr + [candidates[i]], sumArr + candidates[i], i)
                    visited[i] = False
        backtracking([],0,0)
        return answer

        