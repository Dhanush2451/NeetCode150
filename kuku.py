class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,hi=1,max(piles)
        ans=hi
        while l<=hi:
            m=(l+hi)//2
            t=0
            for i in piles:
                t+=math.ceil(float(i)/m)
            if t<=h:
                ans=m
                hi=m-1
            else:
                l=m+1
        return ans
