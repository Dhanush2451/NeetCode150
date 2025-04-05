class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=len(temperatures)
        ans=[]
        for i in range(s):
            c=1
            j=i+1
            while j<s:
                if temperatures[j]>temperatures[i]:
                    break
                j+=1
                c+=1
            c=0 if j==s else c
            ans.append(c)
        return ans
