class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countt={}
        for c in t:
            countt[c]=1+countt.get(c,0)
        ans,ansl=[-1,-1],float("infinity")
        for i in range(len(s)):
            counts={}
            for j in range(i,len(s)):
                counts[s[j]]=1+counts.get(s[j],0)
                flag=True
                for c in countt:
                    if countt[c]>counts.get(c,0):
                        flag=False
                        break
                if flag and(j-i+1)< ansl:
                    ansl=j-i+1
                    ans=[i,j]
        l,r=ans
        return s[l:r+1] if ansl!=float("infinity") else ""
