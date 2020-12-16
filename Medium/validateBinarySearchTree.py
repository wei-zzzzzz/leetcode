'''
Validate Binary Search Tree
2020_11_22
Time: O(n)
Space: O(1)
思考流程：
1.因為BST若用inorder採訪則其所有node回形成遞增序列
2.因此只要上一個值大於當前的值則回傳錯誤
3.要先設一個 global變數既路上一個點
4.左邊比完換右邊
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.last = None
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        if not self.isValidBST(root.left): return False
        if self.last and root.val <= self.last.val: return False
        self.last = root
        return self.isValidBST(root.right)