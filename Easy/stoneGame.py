'''
Time: O(1)
Space: O(1)

思考流程：
1.輕易地以為只要取頭尾之最大
麻煩點，還要考量如何取才會是最佳解
2.修正其麻煩之處（考量頭尾相同狀況），去比較下一層之關係，但為out of range

重新審思別人的code：（數學問題，當然也可用dp但太過於繁雜 O(n^2) ）
1.不論如何取先取者必定會獲勝
  因piles含為偶數個值，且總和為基數，相當於考量要135取之還是246取之（因雙方要以最佳解取值）
  
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        Alex = 0
        Lee = 0
        while piles != []:
            if piles[-1] > piles[0]:
                Alex += piles.pop(-1)
            elif piles[-1] < piles[0]:
                Alex += piles.pop(0)
            else:
                if piles[-2] > piles[1]:
                    Alex += piles.pop(0)
                else:
                    Alex += piles.pop(-1)
            if piles[-1] > piles[0]:
                Lee += piles.pop(-1)
            elif piles[-1] < piles[0]:
                Lee += piles.pop(0)
            else:
                if piles[-2] > piles[1]:
                    Lee += piles.pop(0)
                else:
                    Lee += piles.pop(-1)
        if Alex > Lee:
            return True
        else:
            return False
'''
