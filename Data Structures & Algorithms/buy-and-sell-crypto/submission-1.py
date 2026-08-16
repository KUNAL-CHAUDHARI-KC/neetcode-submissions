class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1


        minBuy = prices[l]
        max_profit = 0 

        while r < len(prices):

            minBuy = min(minBuy, prices[r])

            profit = prices[r] - minBuy
            r += 1

            max_profit = max(max_profit, profit)

        return max_profit
            


        