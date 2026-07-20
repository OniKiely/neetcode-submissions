class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        result = []

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_dic:
                result = [num_dic[complement], index]
                return result

            num_dic[num] = index

        