class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def res():
            token=tokens.pop()
            if token not in "+-*/":
                return int(token)
            right=res()
            left=res()
            if token=='+':
                return left+right
            elif token=='-':
                return left-right
            elif token=='*':
                return left*right
            elif token=='/':
                return int(left/right)
        return res()
