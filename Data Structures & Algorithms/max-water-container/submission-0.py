class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        i, j = 0, len(heights)-1

        while i < j:
            curWater = (j-i) * min(heights[i], heights[j])
            if curWater > maxWater:
                maxWater = curWater
            
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
                
        return maxWater