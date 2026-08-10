class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {j for j in nums}
        return len(s) < len(nums)