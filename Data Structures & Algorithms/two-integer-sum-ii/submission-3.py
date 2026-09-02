class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1

        while r < len(numbers):
            missing = target - numbers[l]
            if numbers[r] == missing:
                return [l+1, r+1]
            elif numbers[r] < missing and r < len(numbers) - 1:
                r += 1
            else:
                l += 1
                while numbers[l] == numbers[l-1]:
                    l += 1
                r = l + 1
        