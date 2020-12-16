'''
K-th Symbol in Grammar
2020_11_17
Time: O(n)
Space: O(n)
思考流程：
1.用遞迴方式去解
2.先設好最基礎為0
3.去找上一層的位置，看是0（生出01）還是1（生出10）
4.加上k在 mod 2取決生出後要第一個位置還是第二個

較慢方法：（因為太多判斷式）
1.若其長度（K）沒超過一半，直接回傳上一層所在的值
2.若超過一半，這會回傳與上一層相反的值
            
'''
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        K += 1
        return (self.kthGrammar(N-1, K//2)+K )%2
'''
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        numOfLayer = 2 ** (N-1)
        if N == 1:
            return 0
        elif K <= (numOfLayer // 2):
            return self.kthGrammar(N-1, K)
        else:
            exK = K - numOfLayer // 2
            if self.kthGrammar(N-1, exK):
                return 0
            else:
                return 1
'''