class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(' : ')', 
                 '[' : ']',
                 '{' : '}'}
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if stack and pairs[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return not stack

# dry run
# ()[]{}
# stack = (
# ) : stack and pairs[(] == ), stack = []

test = Solution()
print(test.isValid("([{}])"))
