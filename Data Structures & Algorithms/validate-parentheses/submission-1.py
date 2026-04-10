class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top!="[" and i=="]":
                    return False
                if top!="(" and i==")":
                    return False
                if top!="{" and i=="}":
                    return False
        if stack:
            return False
        return True
        