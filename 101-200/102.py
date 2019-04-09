# -*-coding:utf-8-*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if root is [] or root is None:
            return []
        q, top, res = [root], 0, []
        while q:
            count, arr = len(q), []
            while count > 0:
                tmp = q.pop(0)
                arr.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
                count -= 1
            res.append(arr)
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
s = Solution()
a = s.levelOrder(root)
print(a)
