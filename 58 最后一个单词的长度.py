# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLastWord(self, s: str):
        ss = s.strip()
        if not ss:
            return 0
        return len(ss.split(" ")[-1])


obj = Solution()
ans = obj.lengthOfLastWord("   ")
print(ans)
