class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        last_word_length = 0
        for char in reversed(s):
            if char == ' ':
                break
            last_word_length += 1
    
        return last_word_length
        