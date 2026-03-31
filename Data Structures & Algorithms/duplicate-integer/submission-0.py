class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for i in nums:
            mp[i] = 0

        for i in nums:
            mp[i] += 1
            if mp[i] > 1:
                return True
        return False
         