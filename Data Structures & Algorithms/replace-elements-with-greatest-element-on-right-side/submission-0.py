class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans_array = []
        high_num = -1


        for num in reversed(arr):
            ans_array.insert(0, high_num)
            if num > high_num:
                high_num = num

        return ans_array

        