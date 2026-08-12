class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0

        for right in range(len(prices)):
            if prices[left] < prices[right]:
                prifit = prices[right] - prices[left]
                maxP = max(maxP, prifit)
            else:
                left = right

        return maxP
