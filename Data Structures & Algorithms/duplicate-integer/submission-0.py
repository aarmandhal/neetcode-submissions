class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = list(set(nums))
        if len(nums) != len(res):
            return True
        else:
            return False
    



         