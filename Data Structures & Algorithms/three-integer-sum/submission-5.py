class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for n in range(len(nums)):
            if nums[n] > 0:
                break

            if n > 0 and nums[n] == nums[n-1]:
                continue

            left, right = n+1, len(nums)-1
            while left < right:
                total = nums[n] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res. append([nums[n], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return res
                    
