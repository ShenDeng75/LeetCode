#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """以下是提交的代码"""
        val = (l1.val + l2.val) % 10
        over = (l1.val + l2.val) // 10
        l1_n = l1.next
        l2_n = l2.next
        ans = ListNode(val)
        p = ans
        while True:
            if not l1_n and not l2_n:  # 都为空时退出
                if over == 1:  # 当最后一位有进位时
                    p.next = ListNode(1)
                return ans

            if not l1_n:   # l1为空时
                l1_val = 0
            else:
                l1_val = l1_n.val
                l1_n = l1_n.next
            if not l2_n:   # l2为空时
                l2_val = 0
            else:
                l2_val = l2_n.val
                l2_n = l2_n.next
            val = (l1_val + l2_val + over) % 10
            over = (l1_val + l2_val + over) // 10
            node = ListNode(val)
            p.next = node
            p = node


def list2node(ls):
    """list转ListNode，用来测试"""
    obj = ListNode(ls[0])
    p = obj
    for l in range(1, len(ls)):
        nextNode = ListNode(ls[l])
        p.next = nextNode
        p = nextNode
    return obj


if __name__ == "__main__":
    ls_1 = [0]
    ls_2 = [0]
    ln_1 = list2node(ls_1)
    ln_2 = list2node(ls_2)
    obj = Solution()
    ans = obj.addTwoNumbers(ln_1, ln_2)
    pass
