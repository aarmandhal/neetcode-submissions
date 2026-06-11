class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if len(result) == 2:
                break
            for j in range(len(nums)):
                if nums[j] == difference and j != i:
                    result.append(i)
                    result.append(j)
        
        return result
        