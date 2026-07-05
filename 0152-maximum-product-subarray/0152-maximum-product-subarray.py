class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n= len(nums)
        res=nums[0]
        max_pro=nums[0]
        min_pro=nums[0]
        
        for i  in range(1,n):
            number=nums[i]
            if number<0:
                max_pro,min_pro=min_pro,max_pro
            max_pro =max(number,max_pro*number)
            min_pro=min(number,min_pro*number)
            res=max(res,max_pro)
        return res       
        
       
        