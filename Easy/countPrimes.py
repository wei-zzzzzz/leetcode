'''
Count Primes
2020_11_24
Time: O(n)
Space: O(n)
思考流程：
大方向 -> 全部減掉小質數（根號n以前）之倍數，並用排容來解決多扣的問題
僅需考慮到根號n是因為數學定理
1.若小於2直接回傳 0
2.建立一個預設全都為1的 list（1表為質數，反之不為質數）
3.但0、1不是質數所以設為０
4.從2至根號n，將其倍數設為0，重複設0並不會有影響（不用考慮排容）
5.回傳有幾個1
'''
class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        s = [1] * n
        s[0] = 0
        s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i : n : i] = [0] * len(s[i * i:n:i])
        return sum(s)
