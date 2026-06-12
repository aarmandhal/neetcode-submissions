class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}

        for i, n in enumerate(nums):
            positions[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in positions and positions[diff] != i:
                return [i, positions[diff]]        
        
        return []