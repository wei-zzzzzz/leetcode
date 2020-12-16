'''
Divide Two Integers
2020_12_10
Time: O(n)
Space: O(1)
思考流程：
1.前處理為標記好sign，然後將小於零之值行絕對值
2.若用一次次扣下去會超過時間，所以改用倍數成長
3.判斷符號以及溢位問題
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        ans = 0
        if dividend < 0 :
            dividend = abs(dividend)
            sign = -sign
        if divisor < 0 :
            divisor = abs(divisor)
            sign = -sign
            
        while dividend >= divisor:
            val, n = divisor, 1
            while val + val <= dividend:
                val += val
                n += n
            ans += n
            dividend -= val
        
        if sign == 1:
            return min(ans, 2**31 -1)
        else: 
            return max(-ans, -2**31)