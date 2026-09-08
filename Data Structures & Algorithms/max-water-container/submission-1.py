class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        maxWater = 0;

        while left < right:
            width = right - left
            currentWater = min(heights[left], heights[right]) * width
            if currentWater > maxWater:
                maxWater = currentWater
            #print(currentWater, "Left: ", left, heights[left], "Right: ", right, heights[right])

            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1

        return(maxWater)