class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {j for j in nums}
        if len(s) < len(nums):
            ans = True
            return ans
        elif len(s) == len(nums):
            ans = False
            return ans