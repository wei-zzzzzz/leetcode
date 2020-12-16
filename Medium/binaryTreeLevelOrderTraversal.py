'''
Binary Tree Level Order Traversal
2020_11_26
Time: O(n)
Space: O(n)
思考流程：
1.用BFS跑向每點
2.要用兩個list記錄每層，一個是記錄tree另個則是值
3.回傳所有值
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels 
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        helper(root, 0)
        return levels
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        else: ans = [[root.val]]
        thislevel = [root]
        while thislevel:
            nextlevel = list()
            nextLevelVal = []
            for n in thislevel:
                if n.left: 
                    nextlevel.append(n.left)
                    nextLevelVal.append(n.left.val)
                if n.right:
                    nextlevel.append(n.right)
                    nextLevelVal.append(n.right.val)
            thislevel = nextlevel
            if nextLevelVal:
                ans += [nextLevelVal]
        return ans
'''