class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        i = 0

        while i < len(nums) - 2:
            target = - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target and [nums[i], nums[j], nums[k]] not in output:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
            
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        
        return output