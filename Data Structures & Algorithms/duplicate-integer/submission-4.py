class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = defaultdict(int)

        for i in nums:
            if not s[i]:
                s[i] = 1
            else:
                return True
        
        return False


        