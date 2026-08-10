class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        k = 0
        while k < 2:
            for j in nums:
                ans.append(j)
            k += 1
        return ans