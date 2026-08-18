class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in numset:
            lenghth = 0
            if (n-1) not in numset:
                lenghth = 0
                while (n+lenghth) in numset:
                    lenghth += 1
            longest = max(longest, lenghth)
        return longest
