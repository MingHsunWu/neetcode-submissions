class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        res = defaultdict(int)
        for c in nums:
            res[c] = res[c] + 1
        for i in range(k):
            ans.append(max(res, key=res.get))
            del res[max(res, key=res.get)]


        return ans