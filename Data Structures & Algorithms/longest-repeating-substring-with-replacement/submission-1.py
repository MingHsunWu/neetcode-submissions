class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_s = 0
        l = 0
        ans = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_s = max(max_s, count.get(s[r]))
            while (r-l+1) - max_s > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans