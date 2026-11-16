class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #no duplicates means use set?
        res = set()
        nums.sort()

        #loop through numbers and if the sum is 0 add to res (set will keep uniqueness)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
        print(res)
        return list(res)
