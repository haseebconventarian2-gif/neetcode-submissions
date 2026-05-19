class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                # We found something that was already stored!
                return True
            seen.add(x)
        return False