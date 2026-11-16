class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #loop through list of nums 
        #map number sequences to how long they are
        #ex. [2, 3, 4, 5] : 4
        #then loop through all values and print largest

        numSet = set(nums)
        result = 0

        for num in numSet:
            if num - 1 not in numSet:
                currentNum = num
                count = 1
                while currentNum + 1 in numSet:
                    currentNum += 1
                    count += 1
                result = max(result, count)
        
        return result


            