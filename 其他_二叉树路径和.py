import copy


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 构造二叉树
def ls2tree(i: int, ls: list):
    if str(ls[i]) == '#':
        return
    root = TreeNode(ls[i])
    root.left = ls2tree(2*i+1, ls)
    root.right = ls2tree(2*i+2, ls)
    return root


# 计算
def col(root: TreeNode, sum_: int, ans: int, res_: list):
    sum_ += root.val
    res_.append(root.val)
    if not root.left and not root.right:
        if sum_ == ans:
            res.append(res_)
        return
    col(root.left, sum_, ans, copy.deepcopy(res_))
    col(root.right, sum_, ans, copy.deepcopy(res_))


tree = ls2tree(0, [10, 5, 12, 4, 7, '#', '#', '#', '#', '#', '#'])
res = []
col(tree, 0, 22, [])
print(res)
