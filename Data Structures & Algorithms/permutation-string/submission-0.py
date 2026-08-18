class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt = defaultdict(int)
        for ch in s1:
            cnt[ch] += 1

        left = 0
        for right in range(len(s2)):
            ch = s2[right]
            cnt[ch] -= 1

            while cnt[ch] < 0:
                cnt[s2[left]] += 1
                left += 1

            if (right-left+1) == len(s1):
                return True

        return False