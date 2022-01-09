#question https://leetcode.com/problems/sorting-the-sentence/submissions/
class Solution:
    def sortSentence(self, s: str) -> str:
        split= s.split()
        answer=''
        words={} 
        
        for i in split:
            words[i[-1]]= i[:-1]
        for i in sorted(words):
            answer=answer+''.join(words[i])+' '
        return answer[:-1]
        
        
