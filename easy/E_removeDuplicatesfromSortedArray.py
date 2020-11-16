'''
Remove Duplicates from Sorted Array
2020_11_9
Time: O(n)
Space: O(1)
思考流程：
1.用i記錄未重複部分;j則是負責跑完整條list
2.將不一樣的值存放回前面重複(i+1)的部分
3.若遇到一樣j就會繼續往下跑
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
#error 
#space: O(n)
#time: O(n^2)
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
