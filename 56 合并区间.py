#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 每次尝试把相邻的两个区间合并，直到所有的相邻区间不能合并。ps: 更好地方法是根据哪边排序就从哪边开始遍历。
class Solution:
    def merge(self, intervals):
        ans = intervals
        while True:
            intervals = self.recur(intervals)
            if intervals == ans:
                break
            ans = intervals
        return ans

    def recur(self, intervals):
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[1])
        ans = []
        merg = intervals[0]
        n = len(intervals)
        for i in range(1, n):
            if merg[1] >= intervals[i][0]:
                merg = [min(merg[0], intervals[i][0]), intervals[i][1]]
            else:
                ans.append(merg)
                merg = intervals[i]
        ans.append(merg)
        return ans
