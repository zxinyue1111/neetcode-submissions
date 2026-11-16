class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create 2 hashmaps, one for s, one for t
        #increment if character is duplicate, add if not
        #compare 2 hashmaps to see if they are the same

        smap = {}
        tmap = {}

        for char in s:
            if char in smap:
                smap[char] += 1
            else:
                smap[char] = 1

        for char in t:
            if char in tmap:
                tmap[char] += 1
            else:
                tmap[char] = 1

        if smap == tmap:
            return True

        return False