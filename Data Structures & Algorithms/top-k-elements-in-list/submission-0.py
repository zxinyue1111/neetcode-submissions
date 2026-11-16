class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use a hashmap for this?
        #map every occurence of a number, then print the top k
        #loop through values starting from k, decrease every loop until 0?

        result = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            result[num] = 1 + result.get(num, 0)
        for n, c in result.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        