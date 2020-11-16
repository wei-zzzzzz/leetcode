'''
2020_11_2
Time:O(n)
Space: O(n)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 > 0:
            return False
        tempS = []
        ans = False
        for i in s:
            if i == ')':
                if tempS == [] or tempS.pop() != '(':
                    return False
                else:
                    ans = True
            elif i == ']':
                if tempS == [] or tempS.pop() != '[':
                    return False
                else:
                    ans = True
            elif i == '}':
                if tempS == [] or tempS.pop() != '{':
                    return False
                else:
                    ans = True
            else:
                tempS.append(i)
        if tempS != []:
            return False
        return ans
