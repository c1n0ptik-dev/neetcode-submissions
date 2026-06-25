class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = float('inf')

        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            
            profit = prices[i] - min_price
            max_profit = max(profit, max_profit)


        return max_profit
            
            
