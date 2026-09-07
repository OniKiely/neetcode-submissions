class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            # check if only remaining nums are positive. cant make 0 with only positive nums
            if nums[i] > 0:
                break
            # check if same as last num
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            low = i + 1
            high = len(nums) - 1
            while(low < high):
                sum = nums[i] + nums[high] + nums[low]
                if sum == 0:
                    result.append([nums[i], nums[low], nums[high]]) # sort
                    low += 1
                    high -= 1
                    while(low < high and nums[low] == nums[low-1]):
                        low += 1
                    while(low < high and nums[high] == nums[high+1]):
                        high -= 1
                elif sum < 0:
                    low += 1
                else:
                    high -= 1
        i += 1

        return(result)