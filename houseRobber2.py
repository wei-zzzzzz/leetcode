'''
Time: O(`)
Space: O()
解題思路：
1.找出最大值且要大於其兩邊之和，才增加ans
2.加入點設為0且兩旁也為0，避免取之
=>問題很大，取不了最佳解

重新審思別人的code：（運用dp）
1.要分兩類，一個是頭到尾之前一個，另個是第二個到最後一個，因為頭尾相連又不能連續取之
2.紀錄當下最佳解，並探討若新元素與前前個最佳解相加有否超過前一個最加解，同樣的道理「不能連續取值」
'''
＃others
class Solution:
        def rob(self, nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            N = len(nums)
            return max(self.rob_range(nums[0 : N - 1]), self.rob_range(nums[1 : N]))
    
        def rob_range(self, nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            N = len(nums)
            dp = [0] * N
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, N):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]
        
''''              
class Solution:
    def rob(self, nums: List[int]) -> int:
        record = {}
        for add, idex in enumerate(nums):
            record[idex] = add
        ans = 0
        
        time = len(nums) // 2
        t = 0
        while t < time:
            M = max(nums)
            nex = record[M]+1
            if nex == len(nums):
                nex = 0
            if M < (nums[record[M]-1] + nums[nex])  and len(nums) > 3:
                nums[record[M]] = 0
                
            else:
                ans += M
                nums[record[M]] = 0        
                nums[nex] = 0
                nums[record[M]-1] = 0
                t += 1
        return ans
'''
