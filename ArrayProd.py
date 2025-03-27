class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s=len(nums)
        ans=[0]*s
        for i in range(s):
            pro=1
            for j in range(s):
                if i==j:
                    continue
                pro*=nums[j]
            ans[i]=pro
        return ans
