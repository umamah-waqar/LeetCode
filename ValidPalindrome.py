class Solution(object):
    def isPalindrome(self,s):
        normalized_string = ''.join(char.lower() for char in s if char.isalnum())
        return normalized_string == normalized_string[::-1]