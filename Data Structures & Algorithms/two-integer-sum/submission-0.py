class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, k in enumerate(nums):
            for j, m in enumerate(nums):
                if i != j and k+m == target:
                    return sorted([i, j])


