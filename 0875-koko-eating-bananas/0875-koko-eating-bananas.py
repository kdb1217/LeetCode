class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        # output의 어떠한 경우에도 최댓값은 무조건 정렬된 배열의 맨 마지막값 못넘음
        answer = piles[-1]
        
        if len(piles) == h:
            return answer
        else:
            start, end = 1, answer
            pivot = (start +end) // 2
            cnt = 0
            
            while start <= end :
                cnt = 0
                for i in piles:
                    if i % pivot != 0:
                        cnt += i // pivot + 1
                    else:
                        cnt += i // pivot

                if cnt > h:
                    start = pivot + 1
                    pivot = (start + end) // 2
                else:
                    answer = min(pivot, answer)
                    end = pivot - 1
                    pivot = (start + end) // 2
                    

            return answer

                



        
