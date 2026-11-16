class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window and iterate thorough until you find a duplicate?
        #need to be able to compare elements between left and right, only compare to right one?
        #have to check with all subsequent characters
        #use dict to store seen values, check if it exists, if it does return length otherwise add it

        l, r = 0, 0
        maxLength = 0
        seen = {}

        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = 1
                r += 1
                currentLength = r - l
                maxLength = max(maxLength, currentLength)
            else:
                seen.pop(s[l])
                l += 1

        return maxLength

        