class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #find complement target - current

        hashmap = {}

        for i, n in enumerate(nums):
            c = target - n
            if c in hashmap:
                return [hashmap[c], i]
            hashmap[n] = i

        return []