class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #keep a window of all unique characters, increase window size to the right, and shrink from the left if a duplicate is encountered
        #calculate length of window by finding diff of r and l
        #keep track of what you have encountered using a set

        l = 0
        maxLength = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLength = max(maxLength, r - l + 1)
            r += 1
        
        return maxLength


        