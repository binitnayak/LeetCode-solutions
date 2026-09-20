class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_profit=prices[0]
        maximum=0
        profit=0
        for p in prices:
            min_profit=min(min_profit,p)
            profit=(p-min_profit)
            maximum=max(maximum,profit)
        return maximum