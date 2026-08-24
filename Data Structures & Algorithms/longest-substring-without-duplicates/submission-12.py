class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numSet = set()
        left = 0
        maxL = 0

        for right in range(len(s)):
            while s[right] in numSet:
                numSet.remove(s[left])
                left += 1
            numSet.add(s[right])
            maxL = max(maxL, right-left+1)

        return maxL