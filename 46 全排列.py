# -*- coding: utf-8 -*-
import copy


class Solution:
    def permute(self, nums):
        self.res = []
        self.nums = nums
        tab = [0 for _ in range(len(nums))]
        re = []
        self.resv(tab, re)
        return [x for x in self.res if len(x) == len(nums)]

    def resv(self, tab, re):
        for i, e in enumerate(self.nums):
            if tab[i] == 0:
                re.append(e)
                tab[i] = 1
                self.resv(tab, re)
                tab[i] = 0
                re.remove(e)

        self.res.append(copy.deepcopy(re))


# class Solution:   # 更好地做法，使用插入遍历
#     def permute(self, nums):
#         l = [[nums[0]]]
#         for i in nums[1:]:
#             l = [j[:k]+[i]+j[k:] for j in l for k in range(len(j)+1)]
#         return l


obj = Solution()
ans = obj.permute([1, 2, 3, 4])
print(ans)
