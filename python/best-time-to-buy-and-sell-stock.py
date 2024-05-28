class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # quick solution but not optimized
        # record_profit=0
        # max_profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)-1):
        #         print(prices[i] , prices[j])
        #         if prices[i] < prices[j]:
        #             record_profit  = prices[j] - prices[i]
        #             if record_profit > max_profit:
        #                 max_profit = record_profit
        # return max_profit
        # buy = 0
        # sell = 1
        # max_profit = 0
        # while sell < len(prices):
        #     current_profit = prices[sell] - prices[buy]
        #     if prices[buy] < prices[sell]:
        #         max_profit = max(current_profit,max_profit)
        #     else: 
        #         buy = sell
        #     sell += 1
        # return max_profit
        min_price = float('inf')
        max_price = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                current_price = price - min_price
                if current_price > max_price:
                    max_price = current_price
        return max_price



            



