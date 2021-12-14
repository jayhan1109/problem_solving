# https://leetcode.com/problems/reorder-data-in-log-files/
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            if log.split(' ')[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key= lambda x: (x.split(' ')[1:], x))
        return letters + digits