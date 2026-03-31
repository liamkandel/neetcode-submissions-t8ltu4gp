class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        ls = [[] for i in range(len(nums) + 1)]

        for n, c in freq.items():
            ls[c].append(n)
        
        result = []

        for lst in ls[::-1]:
            if lst:
                for num in lst:
                    result.append(num)
                if len(result) == k:
                    return result
            