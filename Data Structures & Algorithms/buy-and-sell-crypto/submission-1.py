class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        maxProfit = 0

        while R < len(prices):
            currentProfit = prices[R] - prices[L]
            if currentProfit > maxProfit:
                maxProfit = currentProfit

            if prices[L] > prices[R]:
                L = R
            
            R += 1
        
        return maxProfit

        