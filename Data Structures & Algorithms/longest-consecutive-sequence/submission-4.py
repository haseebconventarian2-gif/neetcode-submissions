class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)

        current_length = 1
        max_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] == nums[i - 1] + 1:
                current_length = current_length + 1
                max_length = max(max_length, current_length)

            else:
                current_length = 1

        return max_length