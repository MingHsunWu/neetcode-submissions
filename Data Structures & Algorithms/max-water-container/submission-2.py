class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        w = r - l
        h = min(heights[l], heights[r])
        ans = w * h
        while l < r:
            if heights[l] < heights[r]:
                l += 1
                w = r - l
                h = min(heights[l], heights[r])
                ans = max(ans, w*h)
            elif heights[l] > heights[r]:
                r -= 1
                w = r - l
                h = min(heights[l], heights[r])
                ans = max(ans, w*h)
            else:
                l += 1
                r -= 1
                w = r - l
                h = min(heights[l], heights[r])
                ans = max(ans, w*h)
        return ans