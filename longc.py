class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        inputs=set(nums)
        res=0
        for i in inputs:
            if(i-1) not in inputs:
                ans=1
                while(i+ans) in inputs:
                    ans+=1
                res=max(ans,res)
        return res
