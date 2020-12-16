'''
Min Stack
2020_11_30
Time: O(1)
Space: O(n)
思考流程：
1.用 list當作 stack
比較需要探討為getMin，若直接用min()這API，時間回來到O(n)
2.多創一個空間紀錄當下最小值，到時可直截回傳最後一項，時間達到O(1)

'''
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minValue = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minValue.append(min(x, self.minValue[-1]) if self.minValue else x)
    def pop(self) -> None:
        self.minValue.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValue[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()