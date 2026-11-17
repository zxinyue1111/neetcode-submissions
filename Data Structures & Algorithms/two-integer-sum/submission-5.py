class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use a hashmap and find if the complement exists
        #use the index of the int as the value of hashmap

        res = {}

        for i, n in enumerate(nums):
            c = target - n

            if c in res:
                return [res[c], i]
            
            res[n] = i

        return []