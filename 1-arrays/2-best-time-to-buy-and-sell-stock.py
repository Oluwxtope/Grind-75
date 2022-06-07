class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        max_profit = 0
        length = len(prices)
        while end < length:
            if prices[end] < prices[start]:
                start = end
                end = start + 1
            else:
                curr_profit = prices[end] - prices[start]
                max_profit = max(curr_profit, max_profit)
                end += 1
        return max_profit