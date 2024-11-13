class Solution:
    # 계수 정렬
    def sortColors(self, nums: List[int]) -> None:
        arr = [0] * 3
        idx = 0

        for i in nums:
            arr[i] += 1

        for j in range(len(arr)):
            for k in range(arr[j]):
                nums[idx] = j
                idx += 1

    


            
        
        