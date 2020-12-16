'''
Symmetric Tree
2020_11_23
Time: O(n)
Space: O(1)
思考流程：
 1.若為空樹直接回傳true
 2.遞迴比較左子點與右子點
遞迴部分
 3.基礎為跑到最底層則回傳true
 4.若左與右不一則回傳false（不一包含左有右沒有子或相反又或著其值不相同）
 5.往左之左與右之右遞迴 和 左之右與右之左遞迴
 '''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.subSymmetric(root.left, root.right)

    def subSymmetric(self, left, right):
        if not left and not right:
            return True
        if (left and not right) or (not left and right) or (left.val != right.val):
            return False;
        return self.subSymmetric(left.left, right.right) and self.subSymmetric(left.right, right.left)
    
    