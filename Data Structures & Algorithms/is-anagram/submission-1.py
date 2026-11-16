class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #2 dicts, and see if they are identical
        #return True if yes, False if no

        dict1 = {}
        dict2 = {}

        #2 for loops to go through each string respectively

        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for char in t:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1   

        return dict1 == dict2    
        