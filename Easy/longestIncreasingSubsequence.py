'''
2020_10_31
Time: O(n^2)
Space: O(n)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = [1]*len(nums)
        Max = 0
        if len(nums) <= 1:
            return len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[i] <= length[j]:
                        length[i] = length[j] + 1
            Max = max(Max, length[i]) 
        
        return Max
    
