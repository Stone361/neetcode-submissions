class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(int)

        for ch in s:
            mp[ch] += 1
        for ch in t:
            mp[ch] -= 1
        
        for n in mp.values():
            if n != 0:
                return False
        return True
        # 复杂度O(n+m)