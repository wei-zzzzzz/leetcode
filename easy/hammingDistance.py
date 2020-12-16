'''
Hamming Distance
2020_12_3
Time： O(1)
Space： O(1)
思考流程：
1.Hamming Distance是找出不一樣的地方有幾個，故用XOR來做比較兩數
2.轉二進位（一直取餘數）算有幾個1
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cont = 0
        t = x ^ y
        while t:
            cont += (t % 2)
            t = t // 2
        return cont
