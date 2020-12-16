'''
Number of 1 Bits
2020_12_8
Time: O(1)
Space: O(1)
思考流程:
1.比起除法用位元操作會更快
2.一直將n往右移一格
3.中間判斷最後一格時否為1，若是則輸出加1

note:
& 和 and區別在於前者注重值的運算，後者注重敘述之真假
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n > 0:
            if n & 1:
                out += 1
            n >>= 1
        return out

   
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n >0:
            ans += (n % 2)
            n = n // 2
        return ans
'''