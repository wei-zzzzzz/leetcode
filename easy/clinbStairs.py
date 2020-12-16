'''
Climb Stairs
2020_11_28
Time: O(n)
Space: O(n)
思考流程：
1.用沙盤推算法推倒An = An-1 + An-2
(可用遞迴或迴圈)
note:第一種方法可不用先創建好格子並初始化，甚至能修正少了if判斷
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = []
        ans += [1,2]
        for i in range(2,n):
            ans += [ans[i-1] + ans[i-2]]
        return ans[n-1]
        
        '''
        if n < 2:
            return 1
        ans = [1] * n
        ans[1] = 2
        for i in range(2,n):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[-1]
        '''