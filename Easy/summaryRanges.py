'''
10_29
Time: O(n)
Space: O(n)
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        index = 0
        while index < len(nums):
            if index+1 !=len(nums) and nums[index]+1 == nums[index+1]:
                head = index
                tail = index + 1
                while nums[head]+1 == nums[tail]:
                    head += 1
                    tail += 1
                    if tail == len(nums):
                        break
                ans += ['%d->%d' %(nums[index], nums[head])]
                index = tail
            else:
                ans += [str(nums[index])]
                index += 1
        return ans
