class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #find max 2 heights that also have max distance in between

        #[2, 5, 6, 10, 5]
        max = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            #compare left and right pointers then increment/decrement minimum value
            #calculate area then compare to max

            if heights[left] <= heights[right]:
                area = heights[left] * (right - left)
                left += 1
            else:
                area = heights[right] * (right - left)
                right -= 1

            if area > max:
                max = area
            
        return max