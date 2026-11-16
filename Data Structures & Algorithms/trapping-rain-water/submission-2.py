class Solution:
    def trap(self, height: List[int]) -> int:
        #has to be 2 bars that enclose bars with lower height than both
        #i to k where k is at least i + 2 check if between i and k is less than min(heights[i] and heights[k])
        #maybe use two pointer, then add to a total sum every time there is a valid window
        #once you find the next valid height for right pointer, move left pointer to previous i

        if not height: return 0

        totalSum = 0
        currentMax = height[0]
        currentSuffixMax = height[len(height) - 1]

        prefixMax = []
        suffixMax = []

        #3 for loops total
        #loop to find prefix maxes
        for i in range(len(height)):
            currentMax = max(currentMax, height[i])
            prefixMax.append(currentMax)

        #loop to find suffix maxes
        for i in range(len(height) - 1, -1, -1):
            currentSuffixMax = max(currentSuffixMax, height[i])
            suffixMax.append(currentSuffixMax)
        
        #reverse suffix array so it lines up with prefix array
        suffixMax.reverse()

        #loop to calculate total sum
        #check if current index is greater equal to what you're adding
        for i in range(len(height)):
            if height[i] >= min(prefixMax[i], suffixMax[i]):
                continue
            else:
                totalSum += min(prefixMax[i], suffixMax[i]) - height[i]
                print(totalSum)

        return totalSum

        # left = 0
        # right = len(height) - 1

        #calculate water by taking min(left, right) - height[i]

        #len(height) = 10
        #while right < 9
        # while right < len(height):
        #     if right == left + 1:
        #         if height[right] < height[left]:
        #             right += 1
        #             totalSum += min(height[left], height[right]) - height[right - 1]
        #         else:
        #             right += 1
        #             left += 1

        #     if height[right] >= height[left]:
        #         left = right
        #         right += 1

        #     if height[right - 1] >= height[right]:
        #         right += 1
        #         totalSum += min(height[left], height[right]) - height[right - 1]

        # return totalSum

        