class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            # 새로운 인터벌의 시작값보다 인터벌의 마지막값이 작은 경우
            if interval[1] < newInterval[0]:
                result.append(interval)
            # 새로운 인터벌의 끝값보다 인터벌의 시작값이 큰 경우
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # 병합을 해야하는 경우
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        result.append(newInterval)
        return result

