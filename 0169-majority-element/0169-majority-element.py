class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candi = None
        for num in nums:
            if count ==0:
                candi = num
            count +=1 if num ==candi else -1 
        return candi