class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_i = 0
        max_profit = 0

        for cur_sell_i in range(1, len(prices)):
            if prices[min_buy_i] > prices[cur_sell_i]:
                min_buy_i = cur_sell_i
                continue
            cur_profit = prices[cur_sell_i] - prices[min_buy_i]
            if cur_profit > max_profit:
                max_profit = cur_profit

        return max_profit

            