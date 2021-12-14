# https://leetcode.com/problems/most-common-word/
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r"\W", " ", paragraph)
        
        words = [word for word in paragraph.lower().split()]
        wordMap = {}
        
        for word in words:
            if word in wordMap:
                wordMap[word] += 1
            else:
                wordMap[word] = 1
        
        wordFrequencyList = sorted(wordMap.items(), key=lambda x: x[1], reverse=True)
        
        for wordTuple in wordFrequencyList:
            if wordTuple[0] in banned:
                continue
            else:
                return wordTuple[0]