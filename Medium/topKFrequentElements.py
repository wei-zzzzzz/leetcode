'''
Top K Frequent Elements
2020_12_11
Time: O(nlogn)
Space: O(n)
思考流程：
1.用counter這API去計算出現次數，好處是會自動排大小
2.再用most_common抓出出現前多k次得數字
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums)
        for i in count.most_common(k):
            ans += [i[0]]
        return ans
        