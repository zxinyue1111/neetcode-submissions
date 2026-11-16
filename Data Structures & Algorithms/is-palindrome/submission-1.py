class Solution:
    def isPalindrome(self, s: str) -> bool:
        #set a pointer for left and right ends then compare
        #get rid of whitespace
        #can also implement char.isalnum() yourself by checking with ord()
        text = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(text) - 1

        print(text)

        while left <= right:
            if text[left] == text[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True