from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # output의 어떠한 경우에도 최댓값은 무조건 정렬된 배열의 맨 마지막값 못넘음
        answer = max(piles)
        
        if len(piles) == h:
            return answer

        start, end = 1, answer

        while start <= end:
            pivot = (start + end ) // 2
            cnt = sum(ceil(p / pivot) for p in piles)

            if cnt > h:
                start = pivot + 1
            else:
                answer = min(pivot, answer)
                end = pivot - 1

        return answer

        
