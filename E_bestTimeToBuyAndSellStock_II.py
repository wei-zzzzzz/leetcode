'''
Best Time to Buy and Sell Stock II
2020_11_10
Time:O(n)
Space:O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = 0
        sell = 0
        gain = 0
        while sell < len(prices):
            if  sell == len(prices)-1 or prices[sell] > prices[sell+1] :
                gain =  gain + (prices[sell] - prices[buy])
                buy = sell+1
                sell = buy
            else:
                sell += 1
        return gain
