class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dpTable = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dpTable[i] = max(dpTable[i], dpTable[j] + 1)

        return max(dpTable)
            
        