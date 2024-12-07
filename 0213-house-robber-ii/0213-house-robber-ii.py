from collections import deque

class Solution:
    def rob(self, nums: List[int]) -> int:
        answer = 0
        dpTable = [0 for _ in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        elif len(nums) <= 2:
            return max(nums)
        else:
            for i in range(len(nums) - 1):
                if i == 0:
                    dpTable[0] = nums[i]
                else:
                    dpTable[i] = max((dpTable[i - 2] + nums[i]), dpTable[i - 1])
                    
            answer = max(max(dpTable), answer)
            dpTable = [0 for _ in range(len(nums))]
            for i in range(1, len(nums)):
                if i == 1:
                    dpTable[1] = nums[i]
                else:
                    dpTable[i] = max((dpTable[i - 2] + nums[i]), dpTable[i - 1])
            
        answer = max(max(dpTable), answer)
        return answer


                    
        