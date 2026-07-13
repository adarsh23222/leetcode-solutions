class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit=prices[0]
        profit=0
        n=len(prices)
        for i in range(1,n):
            curr_profit=prices[i]-min_profit
            profit=max(curr_profit,profit)
            min_profit=min(min_profit,prices[i])
        return profit    
                      

        