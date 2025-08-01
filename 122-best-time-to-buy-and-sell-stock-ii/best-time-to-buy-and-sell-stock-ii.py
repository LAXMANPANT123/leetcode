class Solution(object):
    def maxProfit(self, prices):
        i = 0
        lo = prices[0]
        hi = prices[0]
        profit = 0
        n = len(prices)

        while i < n-1:
            #buying down graph
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            lo = prices[i]

            #selling up
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            hi = prices[i]
            profit += hi - lo

        return profit
        
        