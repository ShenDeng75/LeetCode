# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        res = ListNode(head.val)
        root = head.next
        p1 = res
        while root:
            p = res
            new = ListNode(root.val)
            if p1.val <= new.val:   # 针对递增的数据
                p1.next = new
                p1 = p1.next

            elif new.val < p.val:
                new.next = p
                res = new
            else:
                while p.next and new.val > p.next.val:
                    p = p.next
                new.next = p.next
                p.next = new
            root = root.next
        return res


def to(ls: list):
    node = ListNode(ls[0])
    p = node
    for i in ls[1:]:
        p.next = ListNode(i)
        p = p.next

    return node


node = to([2, 1, 5, 4, 6])
obj = Solution()
ans = obj.insertionSortList(node)
a = 1


# class Solution:   # 更牛皮的做法
#     def insertionSortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:  # 如果无节点或只有一个节点
#             return head
#         elif not head.next.next:  # 如果刚好两个结点
#             if head.next.val < head.val:  # 更正顺序
#                 head.next.next = head
#                 head = head.next
#                 head.next.next = None
#             return head
#
#         slow, fast = head, head  # 快慢指针找中点
#         while fast.next and fast.next.next:
#             fast = fast.next.next
#             slow = slow.next
#         # 截断并分别递归
#         head2 = slow.next
#         slow.next = None
#         l1 = self.insertionSortList(head)
#         l2 = self.insertionSortList(head2)
#         # 合并
#         head = cur = ListNode(0)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             cur = cur.next
#         cur.next = l1 or l2
#         return head.next
