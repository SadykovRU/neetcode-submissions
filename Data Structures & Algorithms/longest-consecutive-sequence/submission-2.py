class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 in nums_set:
                continue
            else:
                tracker = num
                length = 1
                while tracker + 1 in nums_set:
                    tracker += 1
                    length += 1
                max_length = max(max_length, length)
        
        return max_length

