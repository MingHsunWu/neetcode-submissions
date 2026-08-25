class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        min_num = prices[0]
        for i in range(len(prices)):
            if min_num > prices[i]:
                min_num = prices[i]
            diff = prices[i] - min_num
            if max_diff < diff:
                max_diff = diff
        
        return max_diff