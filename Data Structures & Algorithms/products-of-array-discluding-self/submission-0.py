class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []

        for i in range(len(nums)):
            temp, nums[i] = nums[i], 1
            results.append(int(math.prod(nums)))
            nums[i] = temp

        return results