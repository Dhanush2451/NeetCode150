class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for a in strs:
            ans+=str(len(a))+'#'+a
        return ans
    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1
            res=int(s[i:j])
            i=j+1
            j=i+res
            ans.append(s[i:j])
            i=j
        return ans
