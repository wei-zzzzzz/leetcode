'''
Time: O(n)
Space: O(n)
解題思路：
1.用新的stack(list)裝答案
2.據觀察結果，若item 值是正的，不會與stack 的內容物相撞，可直接append（因為若同為正回往同方向移動，若相異號也會朝向不同方向前進）
3.麻煩點為碰到負號，若stack 為空或是其top 為負，也可直接append
4.解決碰撞，比較stack 之top 與item ，若top較大，item 跳下一個，反之item 較大則pop top，繼續往下比較
5.一樣大的話就pop top且item往下

'''
class Solution(object):
    def asteroidCollision(self, asteroids) -> list:
        ans = []
        for item in asteroids:
            while ans != [] and item < 0 < ans[-1]:
                if ans[-1] < abs(item):
                    ans.pop()
                    continue  #continue for while
                elif ans[-1] == abs(item):
                    ans.pop()
                break
            else:
                ans.append(item)
        return ans
