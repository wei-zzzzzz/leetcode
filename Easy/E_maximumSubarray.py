'''
Maximum Subarray
2020_11_5
Time: O(n)
Space: O(n)
思考流程：
1.建立一個全為0之list（for dp）
2.紀錄當下最好之解可能是當下之值，抑或是前面加上目前的值（要連續）
3.並比較斷斷續續中的最大值，其哪段最大
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        subM = [0]*len(nums)
        subM[0] = nums[0]
        Max = nums[0]
        for i in range(1,len(nums)):
            subM[i] = max(nums[], (subM[i-1]+nums[i]))
            if subM[i] > Max:
                Max = subM[i]
        print(subM)
        return Max    
