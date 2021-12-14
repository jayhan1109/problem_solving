# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        p = 0
        q = len(s) - 1
        
        while p < q:
            s[p], s[q] = s[q], s[p]
            p += 1
            q -= 1
        