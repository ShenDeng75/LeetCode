# -*- coding: utf-8 -*-
import time
import random


def quitsort(lis: list):  # 偷懒的做法，时间较长
    if len(lis) <= 1:
        return lis
    m = lis[len(lis) // 2]
    left = [x for x in lis if x < m]
    right = [x for x in lis if x > m]
    mm = [x for x in lis if x == m]
    return quitsort(left) + mm + quitsort(right)


def myquitsert(lis: list):  # 模拟快排，时间较短，但是没有自带的sorted快
    if len(lis) <= 1:
        return lis
    piv = lis[0]  # 支点
    f = 0  # 头
    e = len(lis) - 1  # 尾
    k = True  # 是否轮到尾
    while f != e:
        if k:
            if lis[e] < piv:
                lis[f] = lis[e]
                k = False
                f += 1
            else:
                e -= 1
            continue
        if not k:
            if lis[f] >= piv:
                lis[e] = lis[f]
                k = True
                e -= 1
            else:
                f += 1

    return myquitsert(lis[:f]) + [piv] + myquitsert(lis[f+1:])


def quick_sort(array):   # 别人的快排
    def recursive(begin, end):
        if begin >= end:
            return
        l, r = begin, end
        pivot = array[l]
        while l < r:
            while l < r and array[r] > pivot:
                r -= 1
            while l < r and array[l] <= pivot:
                l += 1
            array[l], array[r] = array[r], array[l]
        array[l], array[begin] = pivot, array[l]
        recursive(begin, l - 1)
        recursive(r + 1, end)

    recursive(0, len(array) - 1)
    return array


res = quick_sort([3, 1, 4, 6, 5, 2, 6])
print(res)

# ls = list(range(1000000))
# random.shuffle(ls)
#
# s = time.time()
# res = quitsort(ls)
# e = time.time()
# print(e-s)
#
# s = time.time()
# res = myquitsert(ls)
# e = time.time()
# print(e-s)
#
# s = time.time()
# res = quick_sort(ls)
# e = time.time()
# print(e-s)
#
# s = time.time()
# res = sorted(ls)
# e = time.time()
# print(e-s)
