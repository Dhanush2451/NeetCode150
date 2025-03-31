class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            sr=set()
            for j in range(i,len(s)):
                if(s[j] in sr):
                    break
                sr.add(s[j])
            ans=max(ans,len(sr))

        return ans
