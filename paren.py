class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def paranthesis(s:str):
            o=0
            for c in s:
                o+=1 if c=='(' else -1
                if o<0:
                    return False
            return not o
        def res(s:str):
            if n*2==len(s):
                if paranthesis(s):
                    ans.append(s)
                return 
            res(s+'(')
            res(s+')')
        res("")
        return ans
