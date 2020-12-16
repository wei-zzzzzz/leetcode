'''
Fizz Buzz
2020_12_1
Time: O(n)
Space: O(n)
思考流程：
1.先進行公倍數的判斷，餘數為0則為其倍數
2.用else if來避免重複判斷

修改：往後若多一個倍數這樣原本的方法（下者），會要多輸入很多公倍數問題
因此用個字串來直接加長，不必再多設條件
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            Str = ""
            if not i%3 : Str += "Fizz"
            if not i%5 : Str += "Buzz"
            if len(Str) > 0:
                ans += [Str]
            else:
                ans += ["%d" %i]
        return ans

'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if not i % 15:
                ans += ["FizzBuzz"]
            elif not i % 3:
                ans += ["Fizz"]
            elif not i % 5:
                ans += ["Buzz"]
            else:
                ans += ["%d" %i]
        return ans
'''