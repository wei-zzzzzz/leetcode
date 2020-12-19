'''
Sqrt(x)
2020_12_19
Time: O(logn)
Space: O(1)
思考流程：
1.最笨一個一個找
2.用二元搜尋法去找答案用二元搜尋法去找答案
'''
'''            
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(2 ** 16):
            if i * i > x:
                return i - 1
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        
        left, right = 0, x
        
        while left <= right:
            mid = (left + right)//2
            if mid**2 <= x and (mid+1)**2 > x:
                return mid
            elif mid**2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1