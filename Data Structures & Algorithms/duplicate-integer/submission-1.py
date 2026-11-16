class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a dict to track appearances

        res = set()

        #iterate through list and add each digit to dict

        for n in nums:
            if n in res:
                return True
            res.add(n)

        return False
        