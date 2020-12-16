'''
Rotate Image
2020_11_20
Time: O(n)
Space: O(1)
思考流程：（驚嘆）
1.先轉置(transpose -> At)
2.每行再做顛倒排序，便能得出旋轉
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for t in range(n):
            matrix[t] = matrix[t][::-1]