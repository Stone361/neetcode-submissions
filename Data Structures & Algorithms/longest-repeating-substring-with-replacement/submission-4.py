class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        maxL, maxf = 0, 0
        
        left = 0
        for right in range(len(s)):
            cnt[s[right]] += 1
            maxf = max(maxf, cnt[s[right]])

            while (right-left+1) - maxf > k:
                cnt[s[left]] -= 1
                left += 1
            maxL = max(maxL, right-left+1)

        return maxL