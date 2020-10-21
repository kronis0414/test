#.可匹配任何字元, *匹配前一個字元0或多個
#只匹配.
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
            
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        
        return first_match and isMatch(text[1:], pattern[1:])
