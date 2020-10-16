'''
解題思路：
1.若值傳進來是0或本身overflows 就直接回傳，反之將其以絕對值存取
2.用divmod得餘數根除數，餘數放進list (stack)存取，除數則繼續重複操作
3.將list (stack)將值pop出來並呈上10的次方後加總
4.補回正負號
5.遇上問題點：overlows，多加個if加以判斷
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x >= 2**31-1 or x <= -2**31: 
            return 0
        tempL = [];     ans = 0
        q = abs(x)
        while q > 0:
            q, r = divmod(q, 10)
            tempL.append(r)

        for i in range(len(tempL)):
            ans = ans + tempL.pop() * (10 ** i)
        if x < 0:
            ans = -ans
            
        if ans > (2**31) - 1 or ans < -(2**31):
            return 0         
        return ans
'''
#others
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]  #字串直接倒轉
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)
'''
