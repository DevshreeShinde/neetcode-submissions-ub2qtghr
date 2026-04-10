class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index=0
        max_profit=0
        for i in range(1,len(prices)):
            profit=prices[i]-prices[min_index]
            if prices[min_index]>prices[i]:
                min_index=i
            max_profit=max(max_profit,profit)
        return max_profit
        