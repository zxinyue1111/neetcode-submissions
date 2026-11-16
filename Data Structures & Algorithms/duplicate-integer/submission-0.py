class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sorted or unsorted?
        #if sorted just compare next with current
        #create a map and check for value that is > 1?

        map = {}

        for num in nums:
            if num in map:
                return True
            else:
                map[num] = 1

        return False