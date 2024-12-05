class Solution:
    def rob(self, nums: List[int]) -> int:
        dpTable = [0 for _ in range(len(nums))]
        dpTable[0] = nums[0]
        if len(nums) <= 2:
            return max(nums)

        if len(nums) >= 3:
            dpTable[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                if i == len(nums) - 1:
                    dpTable[i] = max((dpTable[i - 2] + nums[i]), dpTable[i - 1])
                else:
                    dpTable[i] = max((nums[i] + dpTable[i - 2]), dpTable[i - 1], nums[i])

        print(dpTable)
        return max(dpTable)
