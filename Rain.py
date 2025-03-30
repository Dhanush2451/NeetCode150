class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n=len(height)
        res=0
        for i in range(n):
            l=r=height[i]
            for j in range(i):
                l=max(l,height[j])
            for j in range(i+1,n):
                r=max(r,height[j])
            res+=min(l,r)-height[i]
        return res
