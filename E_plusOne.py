'''
Plus One
2020_11_7
Time: O(n)
Space: O(1)
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] + 1 == 10:
                if i != 0:
                    digits[i] = 0
                else:
                    digits[i] += 1
            else:
                digits[i] += 1
                break
            i -= 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits
        

