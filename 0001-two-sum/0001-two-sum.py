class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        n=len(nums)
        for i in range(0,n):
            need=target-nums[i]
            if need in dict:
                return dict[need],i
            dict[nums[i]] =i   


            
            
           
        