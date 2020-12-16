'''
Minimum Depth of Binary Tree
2020_10_25
Time: O(n)
Space: O(n)
思考流程：
1.先算出左邊深度，再換右邊的深度
2.若左有子而右沒有則左+1，反之右+1
3.最後取較淺者
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftChild = 0
        rightChild = 0
        if root.left:
            leftChild = self.minDepth(root.left)
        if root.right:
            rightChild = self.minDepth(root.right)
            
        if leftChild and not rightChild:
            return 1 + leftChild
        elif rightChild and not leftChild:
            return 1 + rightChild
        else:
            return min(leftChild+1,rightChild+1)
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
#mine
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        if root.left != None:
            hL = self.minDepth(root.left)
        else:
            hL = float("inf")
        if root.right != None:
            hR = self.minDepth(root.right)
        else:
            hR = float("inf")
        if hL == float("inf") and hR == float("inf"):
            depth = 1
        else:
            depth = min(hL, hR) + 1 

        return depth 
'''