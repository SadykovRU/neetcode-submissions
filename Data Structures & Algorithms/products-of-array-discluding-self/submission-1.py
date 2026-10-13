class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for x in nums]
        prev = 1

        for i in range(1, len(nums)):
            prev = prev * nums[i-1]
            res[i] = res[i] * prev
        
        post = 1
        for i in range(len(nums)-2, -1, -1):
            post = post * nums[i + 1]
            res[i] = res[i] * post

        return res
        