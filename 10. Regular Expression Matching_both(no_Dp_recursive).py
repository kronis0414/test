#.可匹配任何字元, *匹配前一個字元0或多個
#匹配.*

#         text, pattern
#case1      '', ''
#case2      '', 'a'
#case3      'a', ''
#case4      'a', 'a'
class Solution(object):
    def isMatch(self, text, pattern):
    #check case1 and case3
        if not pattern:
            return not text
        #bool(text)  check case2, case4
        first_match = bool(text) and pattern[0] in {text[0], '.'}

        #發現有*
        if len(pattern) > 1 and pattern[1] == '*':
        #分成2步
        #1.不考慮*, 直接匹配pattern下一個字元(即pattern[2]), 不用first_match因為"前一個字元"是指
        #pattern的前一個字元, 跟text完全沒關係
        #2.考慮*, 繼續匹配text的下一個字元
            return self.isMatch(text, pattern[2:]) or \
                (first_match and self.isMatch(text[1:], pattern))
        #沒發現*
        return first_match and self.isMatch(text[1:], pattern[1:])