class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #find max 2 heights that also have max distance in between

        areas = []
        max = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if heights[i] <= heights[j]:
                    area = heights[i] * (j - i)
                    areas.append(area)
                else:
                    area = heights[j] * (j - i)
                    print(area)
                    areas.append(area)

        for a in areas:
            if a > max:
                max = a
        
        return max