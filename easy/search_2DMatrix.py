,,,
Time : O(m+n) 可用二元搜尋法精進
space : O(m*n) 為 m*n矩陣（無法精進）
思考流程：
1.target與前一排的尾巴和後一排的頭做比較（類似夾擠）
2.若比前排的尾大右後排的頭小，再去找target是否存在該排中（只能1:m-1之row）
3.有邊界問題，所以先去頭去尾（直接與第一排跟最後一派單獨比較）
,,,
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if matrix == [] or matrix == [[]]:
            return 0
        if target <= matrix[0][-1]:
            return target in matrix[0]
        if target >= matrix[m-1][0]:
            return target in matrix[m-1]
        for i in range(1,m-1):
            if target > matrix[i-1][-1] and target < matrix[i+1][0]:
                return target in matrix[i]
