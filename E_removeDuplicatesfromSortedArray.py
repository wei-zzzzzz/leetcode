'''
Remove Duplicates from Sorted Array
2020_11_9
Time: O(n)
Space: O(1)
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        i = 0
        j = i+1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            else:
                j += 1
        return i+1
'''
        temp = nums[0]
        i = 1 
        while i < len(nums):
            if temp == nums[i]:
                nums.pop(i)
            else:
                temp = nums[i]
                i += 1
        return len(nums)
'''
