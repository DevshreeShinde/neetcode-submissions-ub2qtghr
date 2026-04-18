class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        store = {i - 64: chr(i) for i in range(65, 91)}
        ans=""
        while columnNumber > 0:
            columnNumber -= 1
            ans += store[(columnNumber % 26) + 1]
            columnNumber //= 26
        
        return ans[::-1]