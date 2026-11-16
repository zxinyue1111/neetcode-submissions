class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #split nums in half, then look for common prefix/suffix
        #say index is in first half, look for common suffix, if index is second half look for common prefix
        #look in the array storing prefix/suffix multiply first element of prefix array by first element of suffix array then append

        prefix = []
        suffix = []
        result = []
        i = 0
        
        #need some way to keep track of what index
        for i in range(len(nums)):
            product = 1
            sproduct = 1
            for j in range(i):
                product *= nums[j]
            prefix.append(product)
            for h in range(i + 1, len(nums)):
                sproduct *= nums[h]
            suffix.append(sproduct)

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        
        return result


        