class Solution(object):
    def isMatch(self, text, pattern):
        self.memo = {}
        return  self.run(text, pattern, 0, 0)
    def run(self, text, pattern, i, j):
        ans = False
        if (i, j) in self.memo:
            ans = self.memo[(i, j)]
        else:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = False
                if i < len(text):
                    first_match = pattern[j] in {'.', text[i]}
                if j + 1 < len(pattern) and pattern[j+1] == '*':
                    ans = self.run(text, pattern, i, j + 2) \
                         or (first_match and self.run(text, pattern, i + 1, j))
                else:
                    ans = first_match and self.run(text, pattern, i + 1, j + 1)
            self.memo[(i, j)] = ans
        return ans
        
#memo[i, j]表示text[i]和pattern[j]是否匹配
#buttom-up方式