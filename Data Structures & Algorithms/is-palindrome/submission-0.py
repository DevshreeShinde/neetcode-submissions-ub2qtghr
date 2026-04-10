class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s)-1
        i=0
        while i<end:
            while i < end and not s[i].isalnum():
                i += 1
            while i < end and not s[end].isalnum():
                end -= 1
            if s[i].lower()!=s[end].lower():
                return False
            i+=1
            end-=1
        return True
        