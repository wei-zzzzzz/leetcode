'''
Best Time to Buy and Sell Stock II
2020_11_10
Time:O(n)
Space:O(1)
思考流程：
1.大方向為尋找遞增區間
2.設buy, sell之起點
3.buy之更新為sell點之下一位; sell則是從buy開始（這樣最後一點才不會報錯）
4.一但sell點之值比前一個小便賣出
5.預防完全遞增，要增加判斷如果sell走到最後一點

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
