class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxf = 0
        maxL = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxf = max(maxf, count[s[right]])

            while (right-left+1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            maxL = max(maxL, right-left+1)

        return maxL

