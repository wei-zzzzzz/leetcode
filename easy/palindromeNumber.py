'''
2020_11_3
Time:O(n)
Space: O(n)
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0 or (x!=0 and x%10 == 0):
            return False
        xList = []
        xReverse = x
        while xReverse > 0:
            xList.append(xReverse % 10)
            xReverse = xReverse // 10    
        for i in range(len(xList)):
            xReverse += xList.pop() * 10**i
        return xReverse == x
