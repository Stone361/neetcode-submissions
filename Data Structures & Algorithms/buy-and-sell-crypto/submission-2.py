class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0

        for right in range(len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxP = max(profit, maxP)
            else:
                left = right
        
        return maxP
