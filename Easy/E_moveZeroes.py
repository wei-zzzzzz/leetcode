'''
Move Zeroes
2020_11_16
Time: O(n^2)
Space: O(1)
思考流程：
1.遇到0便pop，並計入遇到幾個0
2.最後再加回所有0
3.pop
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        t = 0
        while i < len(nums):
            if nums == []:
                break
            elif nums[i] == 0:
                nums.pop(i)
                t += 1
            else:
                i += 1
        nums += [0]*t
        
