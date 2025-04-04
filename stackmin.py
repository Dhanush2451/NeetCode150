class MinStack:

    def __init__(self):
        self.stack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        t=[]
        ans=self.stack[-1]
        while(self.stack):
            ans=min(ans,self.stack[-1])
            t.append(self.stack.pop())
        while(len(t)):
            self.stack.append(t.pop())
        return ans
