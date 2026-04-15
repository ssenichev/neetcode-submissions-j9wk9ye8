class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        l, r = 0, 1
        max_profit = prices[r] - prices[l]

        while r < len(prices):
            
            if prices[r] < prices[l]:
                l = r
                max_profit = max(max_profit, prices[r] - prices[l])
            
            if prices[r] - prices[l] > max_profit:
                max_profit = prices[r] - prices[l]

            r += 1

        return max_profit