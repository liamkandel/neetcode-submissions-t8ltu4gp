class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            # if comp in d or comp < 0:
            #     continue
            # else:
            d[comp] = i
        print(d)

        for i in range(len(nums)):
            print(nums[i], nums[i] in d)
            if nums[i] in d and i != d[nums[i]]:
                return [i, d[nums[i]]]
        