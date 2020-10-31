'''
Time: O(n)（左右來回掃一遍）
Space: O(1) （沒有多用額外 space）
解題思考：
1.往右掃若遇到1則將count設為1，for重新計算
2.遇到0，則將count放入其中，紀錄其距離
3.往左掃count不變
4.並比較count與seats，取其小
5.順便找出空位之最大值（這樣就不用再多跑一次n）
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxD = 1; count = 20000
        for i in range(len(seats)):
            if seats[i] == 1:
                count = 1
            elif seats[i] == 0:
                seats[i] = count
                count += 1
                
        for i in range(len(seats)-1,-1,-1):
            if seats[i] == 1:
                count = 1
            else:
                seats[i] = min(seats[i], count)
                maxD = max(seats[i], maxD)
                count += 1
        print(seats)        
        return maxD
