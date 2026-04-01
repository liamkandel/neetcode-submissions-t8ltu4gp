class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        cur = 0

        for i in nums:
            if i-1 in nums:
                continue
            
            while i in nums:
                cur += 1
                i += 1

            if cur > longest:
                longest = cur
            cur = 0

        return longest
