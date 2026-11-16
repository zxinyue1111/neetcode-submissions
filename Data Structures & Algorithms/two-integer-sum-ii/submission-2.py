class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, n in enumerate(numbers):
            c = target - n
            if c in hashmap:
                return [hashmap[c] + 1, i + 1]
            hashmap[n] = i