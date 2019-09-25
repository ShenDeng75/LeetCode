#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 遍历顺序为后中前，数值累加
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode):
        self.ans = 0
        self.recursion(root)
        return root

    def recursion(self, node):
        if node is None:
            return
        self.recursion(node.right)
        node.val += self.ans
        self.ans = node.val
        self.recursion(node.left)
