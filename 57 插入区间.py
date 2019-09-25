# -*- coding: utf-8 -*-


class Solution:
    def insert(self, intervals: list, newInterval: list):
        if not intervals:
            intervals.append(newInterval)
            return intervals
        k = 0  # 用来记录是否插入
        ans = []
        if newInterval[0] <= intervals[0][0]:
            if newInterval[1] >= intervals[0][0]:
                intervals[0] = [newInterval[0], max(newInterval[1], intervals[0][1])]
                k = 1
            else:
                ans.append(newInterval)
                k = 1
        for i in range(len(intervals)):
            if (newInterval[0] >= intervals[i][0]) and\
                    (((i+1) == len(intervals)) or (newInterval[0] <= intervals[i+1][0])) and k == 0:  # 插入新区间
                if intervals[i][1] >= newInterval[0]:
                    intervals[i] = [intervals[i][0], max(intervals[i][1], newInterval[1])]
                    k = 1
                else:
                    intervals.insert(i+1, newInterval)
                    k = 1
            elif k == 0:
                ans.append(intervals[i])

            if k == 1 and (i+1 < len(intervals)):   # 保持新区间连续且不重叠
                if intervals[i][1] >= intervals[i+1][0]:
                    intervals[i+1] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                else:
                    ans.append(intervals[i])
        ans.append(intervals[-1])
        return ans


obj = Solution()
ans = obj.insert([[0, 5], [9, 12]], [7, 16])
print(ans)
