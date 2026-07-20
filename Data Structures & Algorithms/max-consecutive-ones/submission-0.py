class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maxNum = 0

        for num in nums:
            if num == 1:
                current += 1
            if current > maxNum:
                    maxNum = current
            if num == 0:
                current = 0

        return maxNum
