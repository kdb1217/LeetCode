from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dec = deque()
        answers = []

        for i in range(len(nums)):
            if dec and dec[0] == i - k:
                dec.popleft()

            while dec and nums[dec[-1]] < nums[i]:
                dec.pop()

            dec.append(i)

            if i >= k - 1:
                answers.append(nums[dec[0]])

        return answers
        
        # 첫번째 시간 초과 풀이
        # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # dec = deque(nums[:k])
        # maxnum = max(dec)
        # answers = [maxnum]
        # flag = False

        # for i in range(k, len(nums)):
        #     newNum = nums[i]
        #     dec.append(newNum)
        #     lastNum = dec.popleft()
        #     if maxnum == newNum:
        #         flag = True
        #     elif maxnum < newNum:
        #         maxnum = newNum
        #     elif maxnum == lastNum and not flag:
        #         maxnum = max(dec)
        #     answers.append(maxnum)
        #     flag = False
        # return answers