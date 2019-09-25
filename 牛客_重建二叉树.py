# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 根据前序遍历和中序遍历，构造二叉树
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        i = 0
        def divi(node, subtin: list):
            root = TreeNode(node)
            if len(subtin) == 1:
                return root
            left = subtin[:subtin.index(node)]
            right = subtin[subtin.index(node) + 1:]
            nonlocal i
            if len(left) != 0:
                i += 1
                root.left = divi(pre[i], left)
            if len(right) != 0:
                i += 1
                root.right = divi(pre[i], right)
            return root
        ans = divi(pre[i], tin)
        return ans


if __name__ == "__main__":
    sol = Solution()
    ans = sol.reConstructBinaryTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    a = 1
