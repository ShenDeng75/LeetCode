#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s: str):
        max_len = 0
        j = 0
        for i in range(len(s)):
            for _ in range(j, len(s)):
                sub_s = s[i:j+1]
                if self.is_repetition(sub_s):  # 如果有重复的字符
                    break
                if len(sub_s) > max_len:
                    max_len = len(sub_s)
                j += 1
        return max_len

    def is_repetition(self, sub_s: str):
        for i in sub_s:
            if sub_s.count(i) > 1:
                return True
        return False


if __name__ == "__main__":
    s = ""
    obj = Solution()
    ans = obj.lengthOfLongestSubstring(s)
    print(ans)
