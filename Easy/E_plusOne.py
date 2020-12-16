'''
Plus One
2020_11_7
Time: O(n)
Space: O(1)
思考流程：
1.最後一位直接加1
2.考慮進位問題
3.要進位則設為0，且繼續到下一位直到第一位
4.途中萬一不用進位就停止迴圈
5.判斷第一位是否要進位，若需要就得多插入一個於頭
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            digits[i] += 1
            if digits[i] == 10:
                if i != 0:
                    digits[i] = 0
            else:
                break
            i -= 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits
        

