#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list):
        nums3 = nums1 + nums2
        snums3 = sorted(nums3)
        lenght = len(snums3)
        if lenght % 2 == 0:
            ans = (snums3[(lenght // 2)] + snums3[(lenght // 2 - 1)])/2
        else:
            ans = snums3[(lenght // 2)]
        return ans


if __name__ == "__main__":
    obj = Solution()
    ans = obj.findMedianSortedArrays([1, 3], [2])
    print(ans)
