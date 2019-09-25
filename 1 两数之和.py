#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        ans = list()
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans
