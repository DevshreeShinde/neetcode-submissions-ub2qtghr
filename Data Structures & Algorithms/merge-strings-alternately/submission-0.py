class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        start1=0
        start2=0
        ans=""
        i=0
        while start1<len(word1) and start2<len(word2):
            if i==0:
                ans+=word1[start1]
                start1+=1
                i+=1
            else:
                ans+=word2[start2]
                start2+=1
                i=0

        while start1<len(word1):
            ans+=word1[start1]
            start1+=1

        while start2<len(word2):
            ans+=word2[start2]
            start2+=1
        return ans
        