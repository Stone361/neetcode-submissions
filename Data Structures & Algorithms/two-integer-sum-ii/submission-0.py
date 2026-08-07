class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        twoSum = 0
        
        while left < right:
            twoSum = numbers[left] + numbers[right]
            
            if left < right and twoSum > target:
                right -= 1
            elif left < right and twoSum < target:
                left += 1
            elif left == right - 1 and twoSum != target:
                return False
            else:
                return [left+1, right+1]