class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use hashmap where key is the count for every letter, and the value is the words that fit
        #time complexity of O(m x n)

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            #use ascii to convert letter to number? or mod

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())