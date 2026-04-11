class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] *= nums[i-1] * left[i-1]
        print(left)
       
        right = [1] * len(nums)


        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        
        res = []
        for i in range(len(nums)):
            res.append(right[i] * left[i])
        return res
