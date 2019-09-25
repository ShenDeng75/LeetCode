#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 二叉搜索树 -- 中序遍历为升序
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode):
        tree = self.tree(root)
        for t in tree:
            if tree.count(t) > 1:
                return False
        if tree == sorted(tree):
            return True
        return False

    def tree(self, root):
        if not root:
            return []
        return self.tree(root.left) + [root.val] + self.tree(root.right)
