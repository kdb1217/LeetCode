class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 완탐 x 10 ^ 10이기 때문에 너무 오래걸림 
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result

                    
