class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        a=len(heights)
        area=0
        for i in range(a):
            height=heights[i]
            r=i+1
            while r<a and heights[r]>=height:
                r+=1
            l=i
            while l>=0 and heights[l]>=height:
                l-=1
            r-=1
            l+=1
            area=max(area,height*(r-l+1))
        return area
