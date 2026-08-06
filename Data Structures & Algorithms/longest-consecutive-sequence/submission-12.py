class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums. sort()

        max_len = 0
        cur_len = 0

        for p in range(0, len(nums)):
            if nums[p] == nums[p-1] + 1:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1

        return max(max_len, cur_len)