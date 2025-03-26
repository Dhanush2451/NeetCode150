class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            c[i]=1+c.get(i,0)
        arr=[]
        for i,count in c.items():
            arr.append([count,i])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
