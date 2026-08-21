class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxA = 0
        left, right = 0, len(h)-1

        while left < right:
            area = (right-left) * min(h[left], h[right])
            maxA = max(maxA, area)

            if h[left] < h[right]:
                left += 1
            else:
                right -= 1

        return maxA

            
            