'''
Single Number
2020_11_13
Time: O(n)
Space: O(1)
思考流程：
1.大方向 -> 用xor去比較是否有重複（python的xor寫法為：＾）
2.多令個ans = 0，長度為1也可直接操作
3.全比較會剩僅出現1次之值

note:
不必困惑是否會影響彼此間的關聯性，可以想像全部列下來必較也沒關係，一樣會判斷為0

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = num ^ ans
        return ans

        '''
#不好點為要多增加預設狀況（長度為1時）
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            nums[i+1] = nums[i] ^ nums[i+1]
        return nums[i+1]
        '''
