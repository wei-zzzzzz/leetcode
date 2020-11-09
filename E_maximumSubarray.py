'''
Maximum Subarray
2020_11_5
Time: O(n)
Space: O(n)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        subM = [0]*len(nums)
        subM[0] = nums[0]
        Max = nums[0]
        for i in range(1,len(nums)):
            subM[i] = max(nums[i], (subM[i-1]+nums[i]))
            if subM[i] > Max:
                Max = subM[i]
        print(subM)
        return Max    
