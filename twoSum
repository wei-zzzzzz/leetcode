"""
解題思路：
1.用兩個 for迴圈尋找加起來為題目所要的答案即可，換言之此為 rude solution

class Solution(object):
    def twoSum(self, nums, target): 
        error = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    error += 1
        if error == 0:
            print("The list doesn't satisfy the target")

值得學習點：
1.用 enumerate取 list之值與位址
#enumerate可以返回位置與值，甚至可以訂起始值 enumerat(list,100)
2.以dictionary去存位置到時候可直接返回位置
"""
#others
def twoSum(nums, target):
    s = {}
    for i, value in enumerate(nums):
        deviation = target - value
        if deviation in s:
            return(s[deviation],i)
        else:
            s[value] = i


