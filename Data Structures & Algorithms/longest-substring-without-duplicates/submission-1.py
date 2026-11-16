class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window and iterate thorough until you find a duplicate?
        #need to be able to compare elements between left and right, only compare to right one?
        #have to check with all previous elements

        currentLength = 0
        maxLength = 0
        seen = []

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.append(s[j])
                    currentLength += 1
                    maxLength = max(maxLength, currentLength)
            seen.clear()
            currentLength = 0
            print(seen)
        
        return maxLength
        #pwwkew

        

        