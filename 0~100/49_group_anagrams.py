# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        wordMap = {}
        
        for w in strs:
            word = ''.join(sorted(w))
            if word in wordMap:
                wordMap[word].append(w)
            else:
                wordMap[word] = [w]
        return wordMap.values()