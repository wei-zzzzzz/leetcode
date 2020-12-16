'''
2020_10_31
Time: O(n^2)
Space: O(n)
'''
class Solution(object):
    def findNumberOfLIS(self, nums):
        length = [1]*len(nums)
        count = [1]*len(nums)
        longest = 0
        if len(nums) <= 1:
            return len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[i] <= length[j]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j]+1 == length[i]:
                        count[i] += count[j]
            longest = max(Max, length[i]) 
        
        return Max
